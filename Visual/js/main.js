console.log('main.js loaded');
var pathToFile = 'midi/7years.mid'
// var pathToFile = 'midi/JosiahMIDI.mid'

nr = new NoteRoll();

// usage: addNote(pitch, startTime, duration);
// nr.addNote(0, 0, .1);
// nr.addNote(1, 1, 1);
// nr.addNote(5, 12, 2);
nr.addNote(0, 0, .1);
getNotesFromMidi();

function getNotesFromMidi() {
  // read the notes from the midi file
  MidiConvert.load(pathToFile, function(midiData) {
    var numOfTracks = midiData.tracks.length;

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
