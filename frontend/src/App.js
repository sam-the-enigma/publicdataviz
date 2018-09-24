import React, { Component } from 'react';
import './App.css';
import { PieChart, Pie, Label, Cell, Tooltip } from 'recharts';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      data: []
    }
  }

  componentWillMount() {
    fetch('http://127.0.0.1:5000/data')
    .then(response => response.json())
    .then(data => {
      console.info(this.setState({data: data}));
    });
  }

  render() {
    const { data } = this.state;

    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Public Data Viz</h1>
        </header>
        <div className="App-intro">
          {renderPieCharts(data)}
        </div>
      </div>
    );
  }
}

function renderPieCharts(data) {
  data = sortByPunishmentRate(data);
  return data.map((row, index) => renderPieChart(row, index));
}

function sortByPunishmentRate(data){
  return data.sort((a, b) => {
    let aSum = a['prison'] + a['parole'] + a['jail'] + a['felony_probation'];
    let bSum = b['prison'] + b['parole'] + b['jail'] + b['felony_probation'];

    return (b['population'] / bSum) - (a['population'] / aSum);
  })
}

function renderPieChart(row, index) {
  let stateName = row['state']
  delete row['state']
  

  let arr = [];

  for (let key in row) {
    if (row.hasOwnProperty(key)) {
      let value = row[key];

      if (key === 'population') {
        value /= 10;
      }

      arr.push({
        name: key,
        value: value
      });
    }
  }

  let colors = {
      'population': '#FFA500',
      'prison': '#FF0000',
      'parole': '#CC3399',
      'jail': '#000033',
      'felony_probation': '#33FFFF'
  }

  return (
    

    <PieChart width={250} height={250} className='pieChart' key={index}>
      <Tooltip />
      <Pie
        dataKey='value'
        data={arr}
        outerRadius='50%'
      >
        <Label 
          value={stateName} 
          viewBox={{x: 50, y: 500, width: 400, height: 400}}
        />

        {
          arr.map((entry, index) => {
            return (<Cell fill={colors[entry.name]} key={index}/>)
          })
        }
      </Pie>
    </PieChart>
    );
}

export default App;
