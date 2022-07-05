import React from "react";
import { MDBContainer, MDBRow, MDBCol } from "mdbreact";
import UserTable from './UserTable.js'
const Layout = () => {
  return (
    <MDBContainer>
      <MDBRow>
       <MDBCol md="2">Pull Data Forms</MDBCol>
        <MDBCol md="8">
          <UserTable></UserTable>
        </MDBCol>
        <MDBCol md="2">.col-md-4</MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default Layout;