let valenceInterval = null;
let currentEmotion = "none";

document.addEventListener('keyup', e => {
    let audio = document.getElementById("audio")
  if ((e.key === " " || e.code === "Space") &&  !audio.paused) {
    let p = document.getElementById("audio-measures");
    p.innerHTML += audio.currentTime + ",<br/>"
  }
})

function toggleMinimizeInstructions() {
    let div = document.getElementById("description-container")
    let header = document.getElementById("description-header")
    if (div.style.maxHeight) {
        header.innerText = "\u23F6 Instructions for use:"
        div.style.maxHeight = null
    } else {
        header.innerText = "\u23F7 Instructions for use:"
        div.style.maxHeight = div.scrollHeight + "px";
    }
}

function startAnnotate() {
    // annotates current valence value every 100 ms
    valenceInterval = setInterval(annotate, 100);
    $("#audio-options").attr("disabled", true)
}

function stopAnnotate() {
    // stops the annotation process
    if (valenceInterval != null) {
        clearInterval(valenceInterval)
    }
    valenceInterval = null;
}

function annotate() {
    // appends the current time, valence pair to a p tag
    let audio = document.getElementById("audio")
    let p = document.getElementById("audio-valence")
    let div = document.getElementById("audio-valence-container")
    // let i = document.getElementById("valence-slider")
    if (!audio.paused) {
        p.innerHTML += audio.currentTime + " : " + currentEmotion + ",<br/>"
        // p.scrollIntoView(false)
    }
}

function clickEmotion(emotion) {
    let p = document.getElementById("current-category")
    p.innerHTML = "Current category:<br>" + emotion[0].toUpperCase() + emotion.slice(1);
    currentEmotion = emotion
    switch (emotion) {
        case 'anger':
            p.style.backgroundColor = "#c23a22"
            break
        case 'fear':
            p.style.backgroundColor = "#7d54ae"
            break
        case 'sadness':
            p.style.backgroundColor = '#3e65bf'
            break
        case 'none':
            p.style.backgroundColor = '#000000'
            break
        case 'irony':
            p.style.backgroundColor = '#bbbbbb'
            break
        case 'love':
            p.style.backgroundColor = '#ffa0c5'
            break
        case 'joy':
            p.style.backgroundColor = '#f9d476'
            break
    }
    if (['none', 'sadness', 'fear', 'anger'].includes(emotion)) {
        p.style.color = "lightgray"
    } else {
        p.style.color = "black"
    }
}

function restartAnnotate(interval) {
    // resets the time, valence pairs and stops annotation
    stopAnnotate();

    let p;
    let tag;
    if (interval === valenceInterval) {
        p = document.getElementById("audio-valence")
        tag = "valence"
    } else {
        p = document.getElementById("audio-measures")
        tag = "measures"
    }
    e = document.getElementById("audio-options");
    new_file = e.options[e.selectedIndex].text
    $("#audio-options").attr("disabled", false)
    // p.innerHTML = new_file.substring(0, new_file.length - 4) + "_" + tag + " = {"
    p.innerHTML = ""
}

function newAudio() {
    // loads new audio when a new melody is selected
    e = document.getElementById("audio-options");
    new_file = e.options[e.selectedIndex].text
    audio = document.getElementById("audio")
    audio.src = "static/media/" + new_file;

    audio.load()

    p = document.getElementById("audio-valence")
    p.innerHTML = ""
    // p2 = document.getElementById("audio-measures")
    // p.innerHTML = new_file.substring(0, new_file.length - 4) + "_valence = {"
    // p2.innerHTML = new_file.substring(0, new_file.length - 4) + "_measures = {"
}

// function finishValenceAnnotation() {
//     // downloads text file of valence information and disables buttons
//     if (confirm("Download?") === true) {
//         $("#audio-container :input").attr("disabled", true)
//         $("#audio").attr("controls", false)
//         $("#finish-annotate").attr("disabled", true)
//         $("#valence-button-restart").attr("disabled", false)
//
//         file = new Blob([p.innerText], {type: "text/plain"})
//
//         select = document.getElementById("audio-options")
//         name = select[select.selectedIndex].text
//
//         var a = document.createElement("a")
//         a.href = window.URL.createObjectURL(file)
//         a.download = name.substring(0, name.length-4) + "_annotation.txt"
//         a.click()
//     } else {
//         text = "You canceled!";
//     }
// }

async function finishValenceAnnotation() {
    let t, p, e, id;
    if (confirm("Please confirm that you have completed your analysis") === true) {
        p = document.getElementById("audio-valence");
        e = document.getElementById("audio-options");
        t = document.getElementById("custom-textarea");
        id = document.getElementById("id-field")

        new_file = e.options[e.selectedIndex].text

        const data = {
            "piece": new_file,
            "analysis": p.innerText,
            "comments": t.value,
            "custom_id": id.value
        };

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
        let response = await (await fetch('/api/analyses', options)).json()
        console.log(response)

        $("#finish-annotate").attr("disabled", true)
    }
}

document.onkeypress = function(e) {
    if (e.keyCode === 49) { //1
        $("#anger").click().focus()
    } else if (e.keyCode === 50) { //2
        $("#fear").click().focus()
    } else if (e.keyCode === 51) { //3
        $("#sadness").click().focus()
    } else if (e.keyCode === 52) { //4
        $("#none").click().focus()
    } else if (e.keyCode === 55) { //7
        $("#irony").click().focus()
    } else if (e.keyCode === 56) { //8
        $("#love").click().focus()
    } else if (e.keyCode === 57) { //9
        $("#joy").click().focus()
    }
}

// function secondaryEmotion(mainEmotion) {
//     mainButton = document.getElementById(mainEmotion)
//     mainButton.style.backgroundColor = "white"
//     mainButton.style.color = "black"
// }

// $(document).on("keypress", "selector", keyboardEmotionButtons)
addEventListener('playing', startAnnotate)
addEventListener('pause', stopAnnotate)



