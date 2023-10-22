import React, {Component} from 'react';
import '../../CSS/Admin/admin.css';
import DataFetchPost from '../../DataFetchFunctions/DataFetchPost';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import NavBar from '../NavBar/NavBar';

var fileDownload = require('js-file-download');

//This function is associated to the EXPORT button for PDF export
function FileB() {
    //function to handle PDF download
    const handlePDFDownload = () => {
        //fetching PDF data to the server
        DataFetchGet('api/REQ7/send_info/', { 
          responseType: 'blob',
        }).then(res => {
            let data = res.data
            if (data['status'] === 405){
                console.log(data['log'])
                return
            }else if (data['status'] === 500){
                window.location.href="/login";
                window.alert(data['log']);
                return;
            }
            //Downloading the PDF file and naming it "filename.xml"
            fileDownload(res.data['data'], 'filename.xml');
            console.log(res);
        })
        return
}
return (
    //EXPORT button
    <div>
      <div className="ports">
       <button onClick={() => handlePDFDownload()}>EXPORT</button>
       </div>
    </div>
    )
}

//This class is associated to the INPUT button for file upload
class FileA extends Component {

    constructor(props) {
      super(props);
  
      this.state = {
        file: null
      };
    }
   //Handles file input change
    handleInputChange = async (event) => {
      event.preventDefault();
      await this.setState({
        // [event.target.name]: event.target.files[0]
        file: event.target.files[0]
        // image: event.target.files[0]
      });
    };
    //sends file to the server
    async sendFile(state){
      let data = new FormData();
      //alerts when no file is chosen
      if (state.file == null){
          window.alert("No file chosen")
          return 
      }
      data.append("file", state.file);
  
      let a = await DataFetchPost('api/REQ7/load_info/', data)
      
      if (a.data['status'] === 505){
        // If the status code is 505, show an alert with the error message
            window.alert(a.data['log'])
            return
      }else if (a.data['status'] === 500){
        // If the status code is 500, redirects user to Login page and shows an alert with the error message
            window.location.href="/login"
            window.alert(a.data['log'])
            return
      }
      //sends an alert when it is sucessful
      window.alert('Quizzes read successfully!')
      console.log(a);
    }
  
    render() {
      return (
          //IMPORT button
          <div className="ports">
            <input type="file" name="image" onChange={this.handleInputChange} />
            <button onClick={() => this.sendFile(this.state)}>IMPORT</button>
          </div>
      );
    }
}


const Admin = () => {
    return(
        <>
            <NavBar/>
            <FileA/>
            <FileB/>    
        </>
        );
}

export default Admin;

