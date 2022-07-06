import React, { Component } from "react";
import { MDBContainer, MDBRow, MDBCol } from "mdbreact";
import UserTable from './UserTable.js'
import axios from "axios";

export default class Layout extends Component {

  state = {
    data: [],
    next_page_number: null,
    previous_page_number: null
  }

  page = 1
  page_size = 10

  componentDidMount() {
    this.fetchUsersList()
  }

  fetchUsersList() {
    let params = { 
      page: this.page, 
      page_size: this.page_size, 
      id: this.user_id, 
      name: this.user_name, 
      gender: this.user_gender 
    }

    axios({
      url: "http://localhost:8000/api/users/",
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      data: JSON.stringify( params ),
    })
      .then((res) => { 
        
        this.setState( {
          data: JSON.parse( res.data.users ),
          next_page_number: res.data.pagination.next_page_number, 
          previous_page_number: res.data.pagination.previous_page_number 
        } )

      })
      .catch((err) => { });   
  }

  nextPage = () => {
    this.page = this.state.next_page_number
    this.fetchUsersList()
  }

  previousPage = () => {
    this.page = this.state.previous_page_number
    this.fetchUsersList()
  }

  searchUsers = (user_id) => {
    this.page = 1
    this.page_size = 10
    this.fetchUsersList()
  }

  render(){
    return (
      <MDBContainer {...this.props}>
        <MDBRow>
        <MDBCol md="4">
          <div className="form-group">
            <MDBRow>
              <MDBCol md="8">
                <h3>User Filter</h3>
              </MDBCol>
            </MDBRow>
            <MDBRow>
              <MDBCol md="4">
                <label htmlFor="formGroupExampleInput">User Id</label>
              </MDBCol>
             <MDBCol md="4">
              <input
                type="number"
                className="form-control"
                id="user_id"
                onChange={(e) => {this.user_id = e.target.value}}
              />
              </MDBCol>
            </MDBRow>
            <p />
            <MDBRow>
              <MDBCol md="4">
                <label htmlFor="formGroupExampleInput">Name</label>
              </MDBCol>
              <MDBCol md="4">
                <input
                  type="text"
                  className="form-control"
                  id="user_name"
                  onChange={(e) => {this.user_name = e.target.value}}
                />
              </MDBCol>
            </MDBRow>
            <p />
            <MDBRow>
              <MDBCol md="4">
                <label htmlFor="formGroupExampleInput">Gender</label>
              </MDBCol>
              <MDBCol md="4">
                <select className="browser-default custom-select" id="user_gender" onChange={(e) => {this.user_gender = e.target.value}}>
                 <option>Choose your option</option>
                 <option value="male">Male</option>
                 <option value="female">Female</option>
                </select>
              </MDBCol>
            </MDBRow>
            <p />
            <MDBRow>
              <MDBCol md="4">
              </MDBCol>
              <MDBCol md="4">
                <button type="button" className="btn btn-secondary waves-effect waves-light" onClick={() => this.searchUsers(this.user_id)}>Search</button>
              </MDBCol>
            </MDBRow>
          </div>
        </MDBCol>
         <MDBCol md="8">
            <UserTable data={this.state.data}>
            </UserTable>
            <ul className="pagination">
              <li className={"paginate_button page-item previous " + (this.state.previous_page_number == "" ? "disabled" : "")}>
                <a href="#" className="page-link" onClick={() => this.previousPage() }>Previous</a>
              </li>
              <li className={"paginate_button page-item next " + (this.state.next_page_number == "" ? "disabled" : "")}>
                <a href="#" className="page-link"  onClick={() => this.nextPage() }>Next</a>
              </li>
            </ul>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    )
  }

}