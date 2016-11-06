// this is the driver script for the game
// TODO: add more description here later

var i, j, k;
// var pathToFile = 'midi/7years.mid';
var pathToFile = 'midi/pirates.mid';
// var pathToFile = 'midi/JosiahMIDI.mid';


// var offset = 1.6;
var offset = 2.1;
// var offset = 2.4;

// get properties and store in p
p = getProperties();
console.log(p);

// creates the NoteRoll object
var nr = new NoteRoll (100, p);



// read the notes from the midi file
MidiConvert.load(pathToFile, function(midiData) {
  var notesData;

  // console.log(midiData.tracks.length);
  var numOfTracks = midiData.tracks.length;
  // console.log("numOfTracks: ", numOfTracks)
  var totalDurations = 0;

  // loop through all tracks
  for (i = 0; i < numOfTracks; i++) {
    notesData = midiData.tracks[i].notes;
    if (notesData) {
      for (j = 0; j < notesData.length; j++) {
        nr.notes.push(new Note(notesData[j].midi - 21, notesData[j].time, notesData[j].duration, notesData[j].velocity));
        totalDurations += notesData[i].duration;
      }
    }
  }


  // sort the notes by startTime
  nr.sortNotes();

  // assign each note in notes array to a noteGraphic
  nr.assignNoteGraphics();
  nr.assignAnimationProperties(p);

  tl = generateTimeline(nr.notes, nr.keys, p);
  TweenMax.globalTimeScale(1);


  MIDIjs.play(pathToFile);
  // tl.play();

  var played = 0;

  console.log(nr.notes);
  MIDIjs.player_callback = display_time;
  function display_time(player_event) {
    played += 1;
    if (played < 4) {
     tl.play(player_event.time + offset);
    }
  };


  // Set the function as message callback
  MIDIjs.message_callback = display_message;


  // tl.play(1);
  // tl.pause();
});
