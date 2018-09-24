import React, { Component } from 'react';
import './App.css';
import { PieChart, Pie } from 'recharts';

class App extends Component {

  componentWillMount() {
    fetch('http://127.0.0.1:5000/data')
    .then(response => response.json())
    .then(data => {
      console.info(data);
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Public Data Viz</h1>
        </header>
        <div className="App-intro">
          <PieChart width={100} height={100} className='pieChart'>
            <Pie
              dataKey='value'
              data={[{name: 'Group A', value: 400}, {name: 'Group B', value: 300}]}
            >
            </Pie>
          </PieChart>
        </div>
      </div>
    );
  }
}

export default App;
