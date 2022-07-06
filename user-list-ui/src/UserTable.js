import React, { Component }  from 'react';
import axios from "axios";
import UserDetails from './UserDetails.js'

export default class UserTable extends Component {
  state = {
      data: [],
      isShowUserDetails: false,
      user_id: 1
  }

  componentWillReceiveProps(nextProps) {
    this.setState({ data: nextProps.data });  
  }

  componentDidMount() {
  }

  componentDidUpdate() {

  }

  showUserDetails = (user_id ) => {
    this.setState( { isShowUserDetails: true, user_id: user_id } )
  }

  hideUserDetails = () => {
    this.setState( { isShowUserDetails: false, user_id: 0 } ) 
  }

  render() {
    return (
      <div {...this.props}>
        <table className="table w-auto table-striped">
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Username</th>
              <th>Email</th>
              <th>Phone</th>
            </tr>
          </thead>
          <tbody>
            {
              this.state.data.map((item,index) => 
                <tr key={item.id} onClick={() => this.showUserDetails(item.id)}>
                  <td> {item.id}  </td> 
                  <td> {item.name} </td>
                  <td> {item.username} </td>
                  <td> {item.email} </td>
                  <td> {item.phone} </td> 
                </tr>
              )
            }
          </tbody>
        </table>
        {this.state.isShowUserDetails && ( <UserDetails close={() => this.hideUserDetails()} user_id={this.state.user_id}></UserDetails> )}
      </div>
    );
  }
}