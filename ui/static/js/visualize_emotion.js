let DATA;

function download(content, file_name, content_type) {
  // Downloads the provided content to local computer storage
  let a = document.createElement("a")
  let file = new Blob([content], {type: content_type})
  a.href = URL.createObjectURL(file)
  a.download = file_name
  a.click()
}

async function fetchRNTimes(file_name) {
  // fetch the abc data with time annotations
  const response = await fetch(`./static/data/${file_name}.json`)
  const json = await response.json()
  console.log(json)
  return json
}

async function displayPhraseRanges() {
  if (DATA == null) {
      DATA = await cleanData()
  }
  let e = document.getElementById("audio-options");
  let file_name = e.options[e.selectedIndex].text
  let rn_json = await fetchRNTimes(file_name.slice(0, -4))

  let curr_start_i = 0
  let phrase_end = rn_json["phraseend"]

  let test = document.getElementById("debug")
  let ranges = {}
  let phrase_num = 0
  for (let ended_i in phrase_end) {
    ended_i = parseInt(ended_i)
    if (phrase_end[ended_i]) {
      let start = rn_json["time"][curr_start_i]
      let end = rn_json["time"][ended_i + 1]

      let rns = new Set()
      for (let i = curr_start_i; i !== ended_i; i++) {
        console.log([i, rns])
        rns.add(rn_json["numeral"][i])
      }

      ranges[phrase_num] = {
        "start":Math.round(start * 100) / 100,
        "end":Math.round(end * 100) / 100,
        "start_i":curr_start_i,
        "end_i": ended_i,
        "emotion_distribution": getEmotionPercentages(file_name, start, end),
        "harmonies": Array.from(rns.values())
      }

      curr_start_i = ended_i + 1
      phrase_num++
    }
  }
  test.innerText = JSON.stringify(ranges, null, "\t")

  // download(JSON.stringify(ranges, null, "\t"), `${file_name.slice(0, -4)}.json`, 'application/json')
}

async function fetchAnalyses() {
    const response = await fetch("/api/analyses")
    const json = await response.json()
    console.log(json["analyses"])
    return json["analyses"]
}

async function cleanData() {
    let json = await fetchAnalyses()
    let analyses = {}
    for (let row of json) {
        if (row.id in [1, 2, 5, 9]) {
          continue;
        }
        let entry = {}
        for (let item of row['analysis'].split(",\n")) {
            if (item === '') {
                continue
            }
            let split = item.split(" : ")
            entry[split[0]] = split[1]
        }
        if (row['piece'] in analyses) {
                Object.assign(analyses[row['piece']], entry)
        } else {
            analyses[row['piece']] = entry
        }
    }
    return analyses
}

function newAudio() {
    // loads new audio when a new melody is selected
    let e = document.getElementById("audio-options");
    let new_file = e.options[e.selectedIndex].text
    let audio = document.getElementById("audio")
    audio.src = "static/media/" + new_file;
    audio.load()
}

function getEmotionPercentages(piece, start, end) {
  let counts = {
      "anger": 0,
      "fear": 0,
      "sadness": 0,
      "none": 0,
      "irony": 0,
      "love": 0,
      "joy": 0
  }
  let total = 0
  for (const key in DATA[piece]) {
      let k = parseFloat(key)
      if (k < end && k > start) {
          counts[DATA[piece][key]]++;
          total++;
      }
  }
  return [
      Math.round(counts['anger']/total*10000)/100,
      Math.round(counts['fear']/total*10000)/100,
      Math.round(counts['sadness']/total*10000)/100,
      Math.round(counts['none']/total*10000)/100,
      Math.round(counts['irony']/total*10000)/100,
      Math.round(counts['love']/total*10000)/100,
      Math.round(counts['joy']/total*10000)/100
  ]
}


async function graphEmotionDistribution() {
  // Retrieves emotion data and generates pie chart based on distribution
  // load emotion data if not loaded
  if (DATA == null) {
      DATA = await cleanData()
  }

  // Retrieve selected piece and range to find emotion
  let a = document.getElementById("audio-options")
  let s = document.getElementsByClassName("minimum")[0]
  let e = document.getElementsByClassName("maximum")[0]

  let piece = a.options[a.selectedIndex].text
  let start = s.ariaValueNow
  let end = e.ariaValueNow

  graph(getEmotionPercentages(piece, start, end))
}

let calls = 0
let myChart;
function graph(emotion_data) {
  let chart = document.getElementById('chart')
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

/*
 *   This content is licensed according to the W3C Software License at
 *   https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
 *
 *   Desc:   A dual slider widget that implements ARIA Authoring Practices
 */

'use strict';
class Visualize_emotion {
  constructor(domNode) {
    this.isMoving = false;
    this.movingSliderNode = false;

    this.domNode = domNode;

    this.svgNode = domNode.querySelector('svg');
    this.svgPoint = this.svgNode.createSVGPoint();

    this.railNode = domNode.querySelector('.rail rect');
    this.rangeNode = domNode.querySelector('.range rect');

    this.minSliderNode = domNode.querySelector('[role=slider].minimum');
    this.maxSliderNode = domNode.querySelector('[role=slider].maximum');

    this.minSliderValueNode = this.minSliderNode.querySelector('.value');
    this.maxSliderValueNode = this.maxSliderNode.querySelector('.value');

    this.minSliderFocusNode = this.minSliderNode.querySelector('.focus-ring');
    this.maxSliderFocusNode = this.maxSliderNode.querySelector('.focus-ring');

    this.minSliderThumbNode = this.minSliderNode.querySelector('.thumb');
    this.maxSliderThumbNode = this.maxSliderNode.querySelector('.thumb');

    // Dimensions of the slider focus ring, thumb and rail

    this.svgWidth = 1000;
    this.svgHeight = 80;

    this.valueTop = 24;
    this.valueHeight = this.minSliderValueNode.getBoundingClientRect().height;

    this.railHeight = 6;
    this.railWidth = 800;
    this.railY = 42;
    this.railX = 10;

    this.thumbTop = 31;
    this.thumbHeight = 28;
    this.thumbWidth = 28;
    this.thumb2Width = 2 * this.thumbWidth;
    this.thumbMiddle = this.thumbTop + this.thumbHeight / 2;
    this.thumbBottom = this.thumbTop + this.thumbHeight;

    this.focusOffset = 8;
    this.focusY = this.valueTop - this.valueHeight - this.focusOffset + 2;
    this.focusWidth = this.thumbWidth + 2 * this.focusOffset;
    this.focusHeight = this.thumbBottom - this.focusY + this.focusOffset + 2;
    this.focusRadius = this.focusWidth / 8;

    this.svgNode.setAttribute('width', this.svgWidth);
    this.svgNode.setAttribute('height', this.svgHeight);

    this.minSliderFocusNode.setAttribute('y', this.focusY);
    this.maxSliderFocusNode.setAttribute('y', this.focusY);
    this.minSliderFocusNode.setAttribute('width', this.focusWidth);
    this.maxSliderFocusNode.setAttribute('width', this.focusWidth);
    this.minSliderFocusNode.setAttribute('height', this.focusHeight);
    this.maxSliderFocusNode.setAttribute('height', this.focusHeight);
    this.minSliderFocusNode.setAttribute('rx', this.focusRadius);
    this.maxSliderFocusNode.setAttribute('rx', this.focusRadius);

    this.minSliderValueNode.setAttribute('y', this.valueTop);
    this.maxSliderValueNode.setAttribute('y', this.valueTop);

    this.railNode.setAttribute('y', this.railY);
    this.railNode.setAttribute('x', this.railX);
    this.railNode.setAttribute('height', this.railHeight);
    this.railNode.setAttribute('width', this.railWidth + this.thumbWidth);
    this.railNode.setAttribute('rx', this.railHeight / 2);

    this.rangeNode.setAttribute('y', this.railY);
    this.rangeNode.setAttribute('x', this.railX / 2);
    this.rangeNode.setAttribute('height', this.railHeight);
    this.rangeNode.setAttribute('width', 0);

    this.sliderMinValue = this.getValueMin(this.minSliderNode);
    this.sliderMaxValue = this.getValueMax(this.maxSliderNode);
    this.sliderDiffValue = this.sliderMaxValue - this.sliderMinValue;

    this.minSliderRight = 0;
    this.maxSliderLeft = this.railWidth;

    this.minSliderNode.addEventListener(
      'keydown',
      this.onSliderKeydown.bind(this)
    );
    this.minSliderNode.addEventListener(
      'pointerdown',
      this.onSliderPointerdown.bind(this)
    );

    this.minSliderNode.addEventListener('focus', this.onSliderFocus.bind(this));
    this.minSliderNode.addEventListener('blur', this.onSliderBlur.bind(this));

    this.maxSliderNode.addEventListener(
      'keydown',
      this.onSliderKeydown.bind(this)
    );
    this.maxSliderNode.addEventListener(
      'pointerdown',
      this.onSliderPointerdown.bind(this)
    );

    // bind a pointermove event handler to move pointer
    document.addEventListener('pointermove', this.onPointermove.bind(this));

    // bind a pointerup event handler to stop tracking pointer movements
    document.addEventListener('pointerup', this.onPointerup.bind(this));

    this.maxSliderNode.addEventListener('focus', this.onSliderFocus.bind(this));
    this.maxSliderNode.addEventListener('blur', this.onSliderBlur.bind(this));

    this.moveSliderTo(this.minSliderNode, this.getValue(this.minSliderNode));
    this.moveSliderTo(this.maxSliderNode, this.getValue(this.maxSliderNode));
  }

  getSVGPoint(event) {
    this.svgPoint.x = event.clientX;
    this.svgPoint.y = event.clientY;
    return this.svgPoint.matrixTransform(this.svgNode.getScreenCTM().inverse());
  }

  getValue(sliderNode) {
    return parseInt(sliderNode.getAttribute('aria-valuenow'));
  }

  getValueMin(sliderNode) {
    return parseInt(sliderNode.getAttribute('aria-valuemin'));
  }

  getValueMax(sliderNode) {
    return parseInt(sliderNode.getAttribute('aria-valuemax'));
  }

  isMinSlider(sliderNode) {
    return this.minSliderNode === sliderNode;
  }

  isInRange(sliderNode, value) {
    let valueMin = this.getValueMin(sliderNode);
    let valueMax = this.getValueMax(sliderNode);
    return value <= valueMax && value >= valueMin;
  }

  isOutOfRange(value) {
    let valueMin = this.getValueMin(this.minSliderNode);
    let valueMax = this.getValueMax(this.maxSliderNode);
    return value > valueMax || value < valueMin;
  }

  getXFromThumb(node) {
    var points = node.getAttribute('points').split(',');
    return parseInt(points[0]);
  }

  moveSliderTo(sliderNode, value) {
    var valueMax,
      valueMin,
      pos,
      x,
      points = '',
      width,
      secondsValue;

    if (this.isMinSlider(sliderNode)) {
      valueMin = this.getValueMin(this.minSliderNode);
      valueMax = this.getValueMax(this.minSliderNode);
    } else {
      valueMin = this.getValueMin(this.maxSliderNode);
      valueMax = this.getValueMax(this.maxSliderNode);
    }

    value = Math.min(Math.max(value, valueMin), valueMax);

    sliderNode.setAttribute('aria-valuenow', value);
    secondsValue = value;

    pos = this.railX;
    pos += Math.round(
      (value * (this.railWidth - this.thumbWidth)) /
        (this.sliderMaxValue - this.sliderMinValue)
    );

    if (this.isMinSlider(sliderNode)) {
      // update ARIA attributes
      this.minSliderValueNode.textContent = `${Math.floor(secondsValue/60)}:${secondsValue%60}` ;
      this.maxSliderNode.setAttribute('aria-valuemin', value);

      // move the SVG focus ring and thumb elements
      x = pos - this.focusOffset - 1;
      this.minSliderFocusNode.setAttribute('x', x);

      points = `${pos},${this.thumbTop}`;
      points += ` ${pos + this.thumbWidth},${this.thumbMiddle}`;
      points += ` ${pos},${this.thumbBottom}`;
      this.minSliderThumbNode.setAttribute('points', points);

      // Position value
      width = this.minSliderValueNode.getBoundingClientRect().width;
      pos = pos + (this.thumbWidth - width) / 2;
      if (pos + width > this.maxSliderLeft - 2) {
        pos = this.maxSliderLeft - width - 2;
      }
      this.minSliderValueNode.setAttribute('x', pos);
      this.minSliderRight = pos;
    } else {
      // update label and ARIA attributes
      this.maxSliderValueNode.textContent = `${Math.floor(secondsValue/60)}:${secondsValue%60}`;
      this.minSliderNode.setAttribute('aria-valuemax', value);

      // move the SVG focus ring and thumb elements
      x = pos + this.thumbWidth - this.focusOffset + 1;
      this.maxSliderFocusNode.setAttribute('x', x);

      points = `${pos + this.thumbWidth},${this.thumbMiddle}`;
      points += ` ${pos + this.thumb2Width},${this.thumbTop}`;
      points += ` ${pos + this.thumb2Width},${this.thumbBottom}`;
      this.maxSliderThumbNode.setAttribute('points', points);

      width = this.maxSliderValueNode.getBoundingClientRect().width;
      pos = pos + this.thumbWidth + (this.thumbWidth - width) / 2;
      if (pos - width < this.minSliderRight + 2) {
        pos = this.minSliderRight + width + 2;
      }

      this.maxSliderValueNode.setAttribute('x', pos);
      this.maxSliderLeft = pos;
    }

    // Set range rect

    // x = this.getXFromThumb(this.minSliderThumbNode) + this.thumbWidth / 2;
    // width = this.getXFromThumb(this.maxSliderThumbNode) - x + this.thumbWidth / 2;
    // this.rangeNode.setAttribute('x', x);
    // this.rangeNode.setAttribute('width', width);
    graphEmotionDistribution()
  }

  onSliderKeydown(event) {
    var flag = false;
    var sliderNode = event.currentTarget;
    var value = this.getValue(sliderNode);
    var valueMin = this.getValueMin(sliderNode);
    var valueMax = this.getValueMax(sliderNode);

    switch (event.key) {
      case 'ArrowLeft':
      case 'ArrowDown':
        this.moveSliderTo(sliderNode, value - 1);
        flag = true;
        break;

      case 'ArrowRight':
      case 'ArrowUp':
        this.moveSliderTo(sliderNode, value + 1);
        flag = true;
        break;

      case 'PageDown':
        this.moveSliderTo(sliderNode, value - 10);
        flag = true;
        break;

      case 'PageUp':
        this.moveSliderTo(sliderNode, value + 10);
        flag = true;
        break;

      case 'Home':
        this.moveSliderTo(sliderNode, valueMin);
        flag = true;
        break;

      case 'End':
        this.moveSliderTo(sliderNode, valueMax);
        flag = true;
        break;

      default:
        break;
    }

    if (flag) {
      event.preventDefault();
      event.stopPropagation();
    }
  }

  onSliderFocus(event) {
    event.currentTarget.classList.add('focus');
    this.svgNode.classList.add('active');
  }

  onSliderBlur(event) {
    event.currentTarget.classList.remove('focus');
    this.svgNode.classList.remove('active');
  }

  onSliderPointerdown(event) {
    this.isMoving = true;
    this.movingSliderNode = event.currentTarget;
    this.isMinSliderMoving = this.isMinSlider(event.currentTarget);

    event.preventDefault();
    event.stopPropagation();

    // Set focus to the clicked handle
    this.movingSliderNode.focus();
  }

  onPointermove(event) {
    if (
      this.isMoving &&
      this.movingSliderNode &&
      this.domNode.contains(event.target)
    ) {
      var x = this.getSVGPoint(event).x - this.railX;
      if (this.isMinSliderMoving) {
        x = Math.max(0, x - this.thumbWidth / 3);
      } else {
        x = Math.max(0, x - (5 * this.thumbWidth) / 3);
      }
      x = Math.min(x, this.railWidth - this.thumbWidth);
      var value = Math.round(
        (x * this.sliderDiffValue) / (this.railWidth - this.thumbWidth)
      );
      this.moveSliderTo(this.movingSliderNode, value);

      event.preventDefault();
      event.stopPropagation();
    }
  }

  onPointerup() {
    this.isMoving = false;
    this.movingSliderNode = false;
  }
}

// Initialize Multithumb Slider widgets on the page
window.addEventListener('load', function () {
  var slidersMultithumb = document.querySelectorAll('.slider-multithumb');

  for (let i = 0; i < slidersMultithumb.length; i++) {
    new Visualize_emotion(slidersMultithumb[i]);
  }
});

