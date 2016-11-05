function run () {
var pathToFile;
var numOfFiles = document.getElementById('numOfFiles').value;
console.log('numOfFIle: ', numOfFiles);
for (i = 1; i <= numOfFiles; i++) {
  pathToFile = 'input/' + i + '_.mid';
  console.log(pathToFile);
  // read the notes from the midi file
  MidiConvert.load(pathToFile, function(midiData) {
    var notesData;
    var str = '';

    var numOfTracks = midiData.tracks.length;
    console.log("numOfTracks: ", numOfTracks)

    var startTime, duration, pitch, velocity;
    // loop through all tracks
    for (i = 0; i < numOfTracks; i++) {
      notesData = midiData.tracks[i].notes;
      if (notesData) {
        for (j = 0; j < notesData.length; j++) {
          // nr.notes.push(new Note(notesData[j].midi - 21, notesData[j].time, notesData[j].duration));
          // console.log(notesData[j]);
          startTime = Math.floor(notesData[j].time * 100);
          duration = Math.floor(notesData[j].duration * 100);
          pitch = notesData[j].midi;
          velocity = notesData[j].velocity;

          str +=  startTime + ' ' + duration + ' ' + pitch + ' ' + velocity + '\n';
        }
      }
    }

    console.log(str);
    console.log('downloading');
    download('out.txt', str);
  });
}

function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

}
