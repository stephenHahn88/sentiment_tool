let valenceInterval = null;
let currentEmotion = null;

document.addEventListener('keyup', e => {
    let audio = document.getElementById("audio")
  if ((e.key === " " || e.code === "Space") &&  !audio.paused) {
    let p = document.getElementById("audio-measures");
    p.innerHTML += audio.currentTime + ",<br/>"
  }
})

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
    let i = document.getElementById("valence-slider")
    if (!audio.paused) {
        p.innerHTML += audio.currentTime + " : " + i.value + "; " + currentEmotion + ",<br/>"
    }
}

function clickEmotion(emotion) {
    currentEmotion = emotion
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
    p.innerHTML = new_file.substring(0, new_file.length - 4) + "_" + tag + " = {"
}

function newAudio() {
    // loads new audio when a new melody is selected
    e = document.getElementById("audio-options");
    new_file = e.options[e.selectedIndex].text
    audio = document.getElementById("audio")
    audio.src = "static/media/" + new_file;

    audio.load()

    p = document.getElementById("audio-valence")
    p2 = document.getElementById("audio-measures")
    p.innerHTML = new_file.substring(0, new_file.length - 4) + "_valence = {"
    p2.innerHTML = new_file.substring(0, new_file.length - 4) + "_measures = {"
}

function finishValenceAnnotation() {
    // downloads text file of valence information and disables buttons
    if (confirm("Download?") === true) {
        p = document.getElementById("audio-valence")
        p.innerHTML += "}"

        $("#audio-container :input").attr("disabled", true)
        $("#audio").attr("controls", false)
        $("#finish-annotate").attr("disabled", true)
        $("#valence-button-restart").attr("disabled", false)

        file = new Blob([p.innerText], {type: "text/plain"})

        select = document.getElementById("audio-options")
        name = select[select.selectedIndex].text

        var a = document.createElement("a")
        a.href = window.URL.createObjectURL(file)
        a.download = name.substring(0, name.length-4) + "_annotation.txt"
        a.click()
    } else {
        text = "You canceled!";
    }
}

function finishMeasureAnnotation() {
    if (confirm("Download?") === true) {
        p = document.getElementById("audio-measures")
        p.innerHTML += "}"

        file = new Blob([p.innerText], {type: "text/plain"})

        select = document.getElementById("audio-options")
        name = select[select.selectedIndex].text

        $("#finish-measures").attr("disabled", true)

        var a = document.createElement("a")
        a.href = window.URL.createObjectURL(file)
        a.download = name.substring(0, name.length-4) + "_measures.txt"
        a.click()
    } else {
        text = "You canceled!";
    }
}

// function secondaryEmotion(mainEmotion) {
//     mainButton = document.getElementById(mainEmotion)
//     mainButton.style.backgroundColor = "white"
//     mainButton.style.color = "black"
// }

addEventListener('playing', startAnnotate)
addEventListener('pause', stopAnnotate)



