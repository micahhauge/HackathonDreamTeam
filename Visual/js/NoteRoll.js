console.log('NoteRoll.js loaded');

/** Definition of NoteRoll class
 * TODO: add a description of the class here
 */
function NoteRoll () {
  this.properties = getProperties();
  this.notes = [];

  // funciton to add a note the the NoteRoll
  this.addNote = function (pitch, startTime, duration) {
    this.notes.push(new Note(pitch, startTime, duration, this.properties));
  }

  // function to render notes
  this.renderNotes = function () {
    // get the last note in the notes array
    var lastNote = this.notes[this.notes.length - 1];
    var endTime = lastNote.startTime + lastNote.duration;
    var endPos = endTime * this.properties.yScale;
    var xPos, yPos, length;

    console.log('End Time: ' + endTime);
    console.log('End px: ' + endPos);
    // loop through all of the notes and place them in their proper positions
    for (var i = 0; i < this.notes.length; i++) {
      length = this.properties.yScale * this.notes[i].duration;
      xPos = (this.notes[i].pitch * this.properties.noteWidth);
      yPos = endPos - (this.notes[i].startTime * this.properties.yScale) - length;
      // console.log('yPos: ', yPos);
      // console.log('xPos: ', xPos);
      // console.log('length: ', length);


      TweenMax.set(this.notes[i].graphic, {
        height: length,
        y: yPos,
        x: xPos,
      });
    }

    console.log('done!');
    this.properties.endPos = endPos;
    this.properties.endTime = endTime;
    this.timeline = createTimeline(this.notes, this.properties);
    // TweenMax.to(window, 0, {scrollTo: endPos});
    // TweenMax.to(window, endTime, {scrollTo: 0});

  }
}

/** Definition of Note class
 * TODO: add a description of the class here
 */
function Note (pitch, startTime, duration, p) {
  this.pitch = pitch;
  this.startTime = startTime;
  this.duration = duration;

  // create graphic
  this.graphic = document.createElement('div');
  this.graphic.className = 'note';

  // add it to the body
  document.body.appendChild(this.graphic);
  TweenMax.set(this.graphic, {
    x: 100,
  });

  return this;

}


// function to add notes in NoteRoll to the DOM in their correct position;
// create the graphic for the note
function createTimeline(notes, p) {
  TweenLite.defaultEase = Linear.easeNone;
  tl = new TimelineMax({paused:true});
  tl.to(window, 0, {scrollTo: p.endPos});
  tl.to(window, p.endTime - 4, {scrollTo: 0}, 0);


  for (var i = 0; i < notes.length; i++) {
    tl.to(notes[i].graphic, .1, {
      backgroundColor: '#00eeff'
    }, notes[i].startTime);
  }

  // tl.to(body)
  return tl;

}

// returns a basic object that contains all of the view dependent information
function getProperties () {
  // p is the object that conatins the properties
  p = {};

  // dimentions of the game view
  p.viewWidth = window.innerWidth;
  p.viewHeight = window.innerHeight;
  p.viewCenter = p.viewWidth / 2;

  p.endPos = null;
  p.endTime = null;

  // establish noteWidth based on viewWidth so that application is scalable
  // p.noteWidth = p.viewWidth / 52;
  p.noteWidth = p.viewWidth / 88;

  // the time in seconds that it will take a note to cross the sceen
  p.noteSpeed = 4;

  // yScale is the number of vertical pixels that represent 1 second in game
  // so if a note is 3 seconds long, it's vertical height will be 3 * yScale pixels
  p.yScale = p.viewHeight / p.noteSpeed;

  return p;
}
