import React, { Component } from 'react';
import axios from "axios";

class UserDetails extends Component {
  state = {
    modal: true,
    user: {}
  }

  componentDidMount() {
    console.log( this.props )
    axios({
      url: "http://localhost:8000/api/user/" + this.props.user_id,
      method: "GET",
      headers: { 'Content-Type': 'application/json' },
    })
      .then((res) => { 
        this.setState( {user: res.data.user})
      })
      .catch((err) => { });
  }

  render() {
    return (
      <div>
        {true && (
          <div className="modal fade show" style={{display: 'block'}}>
            <div className="modal-dialog" role="document">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">User Details</h5>
                </div>
                <div className="modal-body">
                  <table className="table w-auto table-striped">
                    <tbody>
                      <tr>
                        <th>ID</th>
                        <td>{this.state.user.id}</td>
                      </tr>
                      <tr>
                        <th>Name</th>
                        <td>{this.state.user.name}</td>
                      </tr>
                      <tr>
                        <th>Username</th>
                        <td>{this.state.user.username}</td>
                      </tr>
                      <tr>
                        <th>Email</th>
                        <td>{this.state.user.email}</td>
                      </tr>
                      <tr>
                        <th>PhoneNumber</th>
                        <td>{this.state.user.phone}</td>
                      </tr>
                      <tr>
                        <th>City</th>
                        <td>{this.state.user.city}</td>
                      </tr>
                      <tr>
                        <th>State</th>
                        <td>{this.state.user.state}</td>
                      </tr>
                      <tr>
                        <th>Date of Birth</th>
                        <td>{this.state.user.dob}</td>
                      </tr>
                      </tbody>
                  </table>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary waves-effect waves-light" data-dismiss="modal" onClick={this.props.close}>Close</button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    );
  }
}

export default UserDetails;