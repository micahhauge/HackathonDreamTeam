// console.log('main.js loaded');
// var pathToFile = 'midi/7years.mid'
var pathToFile = 'midi/JosiahMIDI.mid'
// var pathToFile = 'midi/lamb.mid'
// TweenMax.defaultEase = Linear.easeNone;

nr = new NoteRoll();

// usage: addNote(pitch, startTime, duration);
// nr.addNote(0, 0, .1);
// nr.addNote(0, 1, 1);
// nr.addNote(2, 2, 2);
// // nr.addNote(0, 0, .1);
// nr.renderNotes();
// nr.timeline.play();
getNotesFromMidi();

function getNotesFromMidi() {
  // read the notes from the midi file
  MidiConvert.load(pathToFile, function(midiData) {
    var numOfTracks = midiData.tracks.length;
    console.log(midiData);

    // loop through all tracks
    for (i = 0; i < numOfTracks; i++) {
      notesData = midiData.tracks[i].notes;
      if (notesData) {
        // test loop
        for (j = 0; j < notesData.length; j++) {
          nr.addNote(notesData[j].midi - 21, notesData[j].time, notesData[j].duration);
        }
      }
    }

    nr.renderNotes();
    nr.timeline.play();

  });

}
