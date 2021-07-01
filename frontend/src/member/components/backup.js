import React, { useState } from 'react'
import { memberLogin } from 'api/index'


const MemberLogin = () => {
  const [login, setlogin] = useState({
    username: '',
    password: ''
  })

  const {username, password} = login

  const handleChange = e => {
    const {name, value } = e.target
    setlogin({
      ...login, 
      [name]: value
    })

  }

  const handleClick = e => {
    e.preventDefault()
    alert('cancled!')
  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`Login info: ${JSON.stringify({...login})}`)
    memberLogin({...login})
    .then(res => {
      alert(`로그인 완료: ${res.data.result}`)
    })
    .catch(err => {
      alert(`로그인 실패: ${err}`)
    })
    
  }

    return (<>
    <h2>Login Form</h2>

<form onSubmit={handleSubmit} method="post">
  <div className="imgcontainer">
    <img src="https://www.w3schools.com/howto/img_avatar2.png" style={{width: "300px"}} alt="Avatar" className="avatar"/>
  </div>

  <div className="container">
    <label labelFor="username"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" onChange = {handleChange} name="username" value={username} required/>

    <label labelFor="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" onChange = {handleChange} name="password" value={password} required/>
        
    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"/> Remember me
    </label>
  </div>

  <div className="container" style={{backgroundColor: "#f1f1f1"}}>
    <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
    <span className="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>
   
    </>)
}