import React, { Component }  from 'react';
import axios from "axios";
import { MDBTable, MDBTableBody, MDBTableHead } from 'mdbreact';

const columns = [
      {
        label: '#',
        field: 'id',
        sort: 'asc',
      },
      {
        label: 'Name',
        field: 'name'
      },
      {
        label: 'Gender',
        field: 'gender'
      },
      {
        label: 'Email',
        field: 'email'
      }
    ];

export default class UserTable extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: []
    };

    axios({
      url: "http://localhost:8000/api/users/",
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      data: JSON.stringify({ page: 1, page_size: 5 }),
    })
      .then((res) => { 
        this.state.data = JSON.parse( res.data.users )
        console.log( this.state.data )
        this.setState( { data: JSON.parse( res.data.users ) } )
      })
      .catch((err) => { });
  }

  componentDidMount() {

  }

  componentDidUpdate() {
    console.log( 'Set State Called' )
  }

  parseData = data => {
    console.log( typeof data.response );
    this.state.data= data.response
  } 

  render() {
    return (
      <MDBTable autoWidth striped>
        <MDBTableHead columns={columns} />
        <MDBTableBody rows={this.state.data} />
      </MDBTable>
    );
  }
}