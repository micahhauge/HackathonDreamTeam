console.log('NoteRoll.js loaded');

// The value of all black notes
var blackNotes = [1,4,6,9,11,13,16,18,21,23,25,28,30,33,35,37,40,42,45,47,49,52,54,57,59,61,64,66,69,71,73,76,78,81,83,85];

// array of all possible pitch values and corresponding Xpos values (works like a dict of ints)
var pitchToXPos = [0,1,1,2,3,3,4,4,5,6,6,7,7,8,8,9,10,10,11,11,12,13,13,14,14,15,15,16,17,17,18,18,19,20,20,21,21,22,22,23,24,24,25,25,26,27,27,28,28,29,29,30,31,31,32,32,33,34,34,35,35,36,36,37,38,38,39,39,40,41,41,42,42,43,43,44,45,45,46,46,47,48,48,49,49,50,50,51];


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

  // function to sort the notes based on startTime
  this.sortNotes = function () {
    var len = this.notes.length;
    var min;
    for (i = 0; i < len; i++) {
      // set minimum to this position
      min = i;

      // check the rest of the array to see if there is anythin smaller
      for (j = i+1; j < len; j++) {
        if(this.notes[j].startTime < this.notes[min].startTime) {
          min = j;
        }
      }

      // if the minimum isn't the position, swap it
      if (i != min) {
        swap(this.notes, i, min);
      }
    }
  }

  // function to render notes
  this.renderNotes = function () {
    this.sortNotes();
    // get the last note in the notes array
    var lastNote = this.notes[this.notes.length - 1];
    var endTime = lastNote.startTime + lastNote.duration;
    var endPos = endTime * this.properties.yScale;
    var xPos, yPos, length, width, xOffset, scale;

    console.log('End Time: ' + endTime);
    console.log('End px: ' + endPos);

    bar(0, this.properties, 'stop');
    bar(endTime, this.properties, 'start');

    this.properties.lastNote = this.notes[this.notes.length - 1];
    this.properties.firstNote = this.notes[0];

    // loop through all of the notes and place them in their proper positions
    for (var i = 0; i < this.notes.length; i++) {

      if (isBlack(this.notes[i].pitch)) {
        xOffset = .5 * this.properties.noteWidth;
        scale = .75;

      } else {
        xOffset = 0;
        scale = 1;
      }
      length = this.properties.yScale * this.notes[i].duration;
      xPos = (pitchToXPos[this.notes[i].pitch] * this.properties.noteWidth) + xOffset;
      yPos = endPos - (this.notes[i].startTime * this.properties.yScale) - length + window.innerHeight;
      nWidth = this.properties.noteWidth * scale;
      // console.log('yPos: ', yPos);
      // console.log('xPos: ', xPos);
      // console.log('length: ', length);

      TweenMax.set(this.notes[i].graphic, {
        height: length,
        width: nWidth,
        y: yPos,
        x: xPos,
      });
    }

    console.log('done!');
    this.properties.endPos = endPos;
    this.properties.endTime = endTime; this.timeline = createTimeline(this.notes, this.properties);
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
  this.graphicColor = null;

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

/** Definition of Note class
 * TODO: add a description of the class here
 */
function bar (time, p, id = "") {
  // create graphic
  this.graphic = document.createElement('div');
  this.graphic.className = 'bar';
  this.graphic.id = id;

  // add it to the body
  document.body.appendChild(this.graphic);
  TweenMax.set(this.graphic, {
    y: time * p.yScale,
  });

  return this;

}


// function to add notes in NoteRoll to the DOM in their correct position;
// create the graphic for the note
function createTimeline(notes, p) {
  console.log(notes);
  TweenMax.defaultEase = Linear.easeNone;

  tl = new TimelineMax({paused:true});


  for (var i = 0; i < notes.length; i++) {
    tl.to(notes[i].graphic, .1, {
      backgroundColor: '#00eeff'
    }, notes[i].startTime - p.firstNote.startTime);
  }

  tl.to(window, 0, {scrollTo: "#start"}, 0);
  tl.to(window, p.endTime, {scrollTo: "#stop", ease: Linear.easeNone}, 0);
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
  p.lastNote = null;
  p.firstNote = null;

  // establish noteWidth based on viewWidth so that application is scalable
  p.noteWidth = p.viewWidth / 52;
  // p.noteWidth = p.viewWidth / 88;

  // the time in seconds that it will take a note to cross the sceen
  p.noteSpeed = 3;

  // yScale is the number of vertical pixels that represent 1 second in game
  // so if a note is 3 seconds long, it's vertical height will be 3 * yScale pixels
  p.yScale = p.viewHeight / p.noteSpeed;

  return p;
}

// function to determine if a key is white or blackNote
function isBlack(pitch) {
 // if the note is black
 if (blackNotes.indexOf(pitch) != -1) {
   return true;
 } else {
   return false;
 }
}

// function to swap two items
function swap(items, firstIndex, secondIndex) {
  var temp = items[firstIndex];
  items[firstIndex] = items[secondIndex];
  items[secondIndex] = temp;
}
