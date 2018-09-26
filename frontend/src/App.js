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

  // componentWillMount() {
  //   console.info('Hello world')

  //   fetch('http://127.0.0.1:5000/data')
  //   .then(response => response.json())
  //   .then(data => {
  //     console.info(data)
  //     this.setState({data: data});
  //   });
  // }

  render() {
    const { data } = this.state;

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

          {/* renderPieCharts(data) */}
        </div>
      </div>
    );
  }
}

// function renderPieCharts(data) {
//   data = sortByPunishmentRate(data);
//   return data.map((row, index) => renderPieChart(row, index));
// }

// function sortByPunishmentRate(data){
//   return data.sort((a, b) => {
//     let aSum = a['prison'] + a['parole'] + a['jail'] + a['felony_probation'];
//     let bSum = b['prison'] + b['parole'] + b['jail'] + b['felony_probation'];

//     return (a['population'] / aSum) - (b['population'] / bSum);
//   })
// }

// function renderPieChart(row, index) {
//   let stateName = row['state']
//   delete row['state']

//   let arr = [];

//   for (let key in row) {
//     if (row.hasOwnProperty(key)) {
//       let value = row[key];

//       if (key === 'population') {
//         value /= 10;
//       }

//       arr.push({
//         name: key,
//         value: value
//       });
//     }
//   }

//   let colors = {
//       'population': '#B7C75A',
//       'prison': '#2F9495',
//       'parole': '#566E8B',
//       'jail': '#6B4761',
//       'felony_probation': '#5B2D30'
//   }

//   return (
//     <PieChart width={350} height={350} className='pieChart' key={index}>
//       <Tooltip />
//       <Pie
//         dataKey='value'
//         data={arr}
//         outerRadius='75%'
//       >
//         <Label
//           value={stateName}
//           viewBox={{x: 50, y: 500, width: 400, height: 400}}
//         />

//         {
//           arr.map((entry, index) => {
//             return (<Cell fill={colors[entry.name]} key={index}/>)
//           })
//         }
//       </Pie>
//     </PieChart>
//     );
// }

export default App;