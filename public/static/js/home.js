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
        header.innerText = "+ Instructions for use:"
        div.style.maxHeight = null
    } else {
        header.innerText = "= Instructions for use:"
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
    // let i = document.getElementById("valence-slider")
    if (!audio.paused) {
        p.innerHTML += audio.currentTime + " : " + currentEmotion + ",<br/>"
    }
}

function clickEmotion(emotion) {
    let p = document.getElementById("current-category")
    p.innerText = "Current category: " + emotion[0].toUpperCase() + emotion.slice(1);
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

function finishValenceAnnotation() {
    if (confirm("Please confirm that you have completed your analysis") === true) {
        p = document.getElementById("audio-valence");
        e = document.getElementById("audio-options");
        t = document.getElementById("custom-textarea");
        new_file = e.options[e.selectedIndex].text

        const data = {
            "piece": new_file,
            "analysis": p.innerText,
            "comments": t.textContent
        };

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
        fetch('/api/analyses', options)
            .then(response => console.log(response.json()))
            .catch(error => {
                console.error('Error:', error)
            })

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



