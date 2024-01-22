import * as Tone from "tone";
import { ToneAudioNode } from "tone";
import RNSToPitches from "/static/data/notes_from_chord.json"
import notesToKeys from "/static/data/notes_to_keys.json"


// Instrument consts
export const piano = new Tone.Sampler({
    urls: {
      "C5": "C5.mp3",
      "D#4": "Ds4.mp3",
      "F#4": "Fs4.mp3",
      "A4": "A4.mp3",
    },
    release: 1,
    baseUrl: "https://tonejs.github.io/audio/salamander/",
  }).toDestination();


export const casio = new Tone.Sampler({
    urls: {
		A1: "A1.mp3",
		A2: "A2.mp3",
	},
    release: 1,
	baseUrl: "https://tonejs.github.io/audio/casio/",
}).toDestination();

interface Note {
    midi: number;
    duration: number;
}

function playVoice(voice: Note[], player: Tone.Sampler) {
    let curr = Tone.now();
    voice.forEach(note => {
        console.log(note.midi);
        // Handle rests
        if (note.midi == -1) {
            curr += Tone.Time(note.duration).toSeconds();
        } else {
            const frequency = Tone.Midi(note.midi).toFrequency();
            player.triggerAttackRelease(frequency, note.duration, curr);
            curr += Tone.Time(note.duration).toSeconds();
        }
    });
}

export function playVoices(melody: [], pitches: number[][], durations: number[][]) {

    let voices: Note[][] = [];
    for (let i=0; i<pitches.length; i++) {
        voices.push([]);
        for (let j=0; j<pitches[i].length; j++) {
            let midi = pitches[i][j];
            let duration = durations[i][j];
            let note = {midi, duration}
            voices[i].push(note);
        }
    }
    
    voices.forEach(voice => {
        playVoice(voice, piano);
    });

}