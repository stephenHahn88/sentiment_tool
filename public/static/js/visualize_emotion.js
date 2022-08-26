function newAudio() {
    // loads new audio when a new melody is selected
    e = document.getElementById("audio-options");
    new_file = e.options[e.selectedIndex].text
    audio = document.getElementById("audio")
    audio.src = "static/media/" + new_file;
    audio.load()
}

function getPercentEmotionsInRange() {
  a = document.getElementById("audio-options")
  s = document.getElementsByClassName("minimum")[0]
  e = document.getElementsByClassName("maximum")[0]

  piece = a.options[a.selectedIndex].text
  start = s.ariaValueNow
  end = e.ariaValueNow
  console.log([start, end])
  const dat = DATA[piece]
  counts = {
      "anger": 0,
      "fear": 0,
      "sadness": 0,
      "none": 0,
      "irony": 0,
      "love": 0,
      "joy": 0
  }
  total = 0
  for (const key in dat) {
      k = parseFloat(key)
      // console.log(dat[key])
      if (k < end && k > start) {
          counts[dat[key]]++;
          total++;
      }
  }
  emotion_data = [
      Math.round(counts['anger']/total*10000)/100,
      Math.round(counts['fear']/total*10000)/100,
      Math.round(counts['sadness']/total*10000)/100,
      Math.round(counts['none']/total*10000)/100,
      Math.round(counts['irony']/total*10000)/100,
      Math.round(counts['love']/total*10000)/100,
      Math.round(counts['joy']/total*10000)/100
  ]
  graph(emotion_data)
}

calls = 0
let myChart;
function graph(emotion_data) {
  chart = document.getElementById('chart')
  if (calls > 0) {
    myChart.destroy()
  }
  const labels = ['Anger', 'Fear', 'Sadness', 'None', 'Irony', 'Love', 'Joy']
  const data = {
      labels: labels,
      datasets: [{
          label: 'test',
          backgroundColor: [
              '#c23a22',
              '#7d54ae',
              '#3e65bf',
              '#000000',
              '#bbbbbb',
              '#ffa0c5',
              '#f9d476'
          ],
          data: emotion_data,
          hoverOffset: 10,
      }]
  };
  const config = {
      type: 'doughnut',
      data: data,
      options: {
        animation: {
          duration: 0
        }
      }
  }
  myChart = new Chart(
      chart,
      config
  )
  calls++;
}