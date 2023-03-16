import * as Tone from "tone";
import RNSToPitches from "/static/data/notes_from_chord.json"
import notesToKeys from "/static/data/notes_to_keys.json"

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

// Buffer for keyup events (needed to re-animate the keyboard)
let keyupEvent1: Event = new KeyboardEvent('keyup', {'key': '`'});
let keyupEvent2: Event = new KeyboardEvent('keyup', {'key': '4'});
let keyupEvent3: Event = new KeyboardEvent('keyup', {'key': '7'});

export function playChord (chord: string) {

    if (Tone.context.state !== 'running') {
        Tone.context.resume();
    }

    // Clear the previous keys
    window.dispatchEvent(keyupEvent1);
    window.dispatchEvent(keyupEvent2);
    window.dispatchEvent(keyupEvent3);

    if (chord === "START" || chord === "PAD") {
        return;
    } else {
        let note1 = RNSToPitches[chord][0];
        let note2 = RNSToPitches[chord][1];
        let note3 = RNSToPitches[chord][2];

        piano.triggerAttackRelease(note1, 1);
        piano.triggerAttackRelease(note2, 1);
        piano.triggerAttackRelease(note3, 1);

        let keydownEvent1 = new KeyboardEvent('keydown', {'key': notesToKeys[note1]});
        let keydownEvent2 = new KeyboardEvent('keydown', {'key': notesToKeys[note2]});
        let keydownEvent3 = new KeyboardEvent('keydown', {'key': notesToKeys[note3]});
        window.dispatchEvent(keydownEvent1);
        window.dispatchEvent(keydownEvent2);
        window.dispatchEvent(keydownEvent3);
    
        // Load up keys for later
        keyupEvent1 = new KeyboardEvent('keyup', {'key': notesToKeys[note1]});
        keyupEvent2 = new KeyboardEvent('keyup', {'key': notesToKeys[note2]});
        keyupEvent3 = new KeyboardEvent('keyup', {'key': notesToKeys[note3]});
    }

}

export function playIChord () {

    window.dispatchEvent(keyupEvent1);
    window.dispatchEvent(keyupEvent2);
    window.dispatchEvent(keyupEvent3);

    piano.triggerAttack("C4", 0);
    piano.triggerAttack("E4", 0);
    piano.triggerAttack("G4", 0);
    piano.triggerRelease("C4", 16);
    piano.triggerRelease("E4", 16);
    piano.triggerRelease("G4", 16);

    let keydownEvent1 = new KeyboardEvent('keydown', {'key': '`'});
    let keydownEvent2 = new KeyboardEvent('keydown', {'key': '4'});
    let keydownEvent3 = new KeyboardEvent('keydown', {'key': '7'});
    window.dispatchEvent(keydownEvent1);
    window.dispatchEvent(keydownEvent2);
    window.dispatchEvent(keydownEvent3);

    // Load up keys for later
    keyupEvent1 = new KeyboardEvent('keyup', {'key': '`'});
    keyupEvent2 = new KeyboardEvent('keyup', {'key': '4'});
    keyupEvent3 = new KeyboardEvent('keyup', {'key': '7'});

}