import * as Tone from "tone";

// Instrument consts
const synth = new Tone.Synth().toDestination();

const piano = new Tone.Sampler({
    urls: {
      "C5": "C5.mp3",
      "D#4": "Ds4.mp3",
      "F#4": "Fs4.mp3",
      "A4": "A4.mp3",
    },
    release: 1,
    baseUrl: "https://tonejs.github.io/audio/salamander/",
  }).toDestination();


const casio = new Tone.Sampler({
    urls: {
		A1: "A1.mp3",
		A2: "A2.mp3",
	},
    release: 1,
	baseUrl: "https://tonejs.github.io/audio/casio/",
}).toDestination();

export function playIChord () {
    let keyupEvent1 = new KeyboardEvent('keyup', {'key': '2'});
    let keyupEvent2 = new KeyboardEvent('keyup', {'key': '4'});
    let keyupEvent3 = new KeyboardEvent('keyup', {'key': '7'});
    window.dispatchEvent(keyupEvent1);
    window.dispatchEvent(keyupEvent2);
    window.dispatchEvent(keyupEvent3);

    piano.triggerAttack("C4", 0);
    piano.triggerAttack("G4", 0);
    piano.triggerRelease("C4", 16);
    piano.triggerRelease("G4", 16);

    let keydownEvent1 = new KeyboardEvent('keydown', {'key': '2'});
    let keydownEvent2 = new KeyboardEvent('keydown', {'key': '4'});
    let keydownEvent3 = new KeyboardEvent('keydown', {'key': '7'});
    window.dispatchEvent(keydownEvent1);
    window.dispatchEvent(keydownEvent2);
    window.dispatchEvent(keydownEvent3);
}

export function playVChord () {
    let keyupEvent1 = new KeyboardEvent('keyup', {'key': '`'});
    let keyupEvent2 = new KeyboardEvent('keyup', {'key': '4'});
    let keyupEvent3 = new KeyboardEvent('keyup', {'key': '7'});
    window.dispatchEvent(keyupEvent1);
    window.dispatchEvent(keyupEvent2);
    window.dispatchEvent(keyupEvent3);

    piano.triggerAttack("B4", 0);
    piano.triggerAttack("A4", 0);
    piano.triggerRelease("B4", 16);
    piano.triggerRelease("A4", 16);

    let keydownEvent1 = new KeyboardEvent('keydown', {'key': '`'});
    let keydownEvent2 = new KeyboardEvent('keydown', {'key': '4'});
    let keydownEvent3 = new KeyboardEvent('keydown', {'key': '7'});
    window.dispatchEvent(keydownEvent1);
    window.dispatchEvent(keydownEvent2);
    window.dispatchEvent(keydownEvent3);
  }