import React , { useState } from 'react'
import './Signup.css'
import { useHistory } from 'react-router'
import { userSignup, userLogin } from 'api/index'

const SignUp = () => {
  const [userInfo, setUserInfo] = useState({
    username: '',
    password: '',
    name: '',
    email: ''
  }) // member를 대표할 수 있는 상태들 JSON을 State에 받아서 State(기능(setUserInfo)과 속성(userInfo)을 포함한 객체를 사용/ JSON을 상태화시킨다

  const {username, password, name, email} = userInfo

  const handleChange = e => {
    const { name, value } = e.target
    setUserInfo({
      ...userInfo,
      [name]: value
    })
  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송 클릭: ${JSON.stringify({...userInfo})}`)
    userSignup({...userInfo}) //userinfo의 값을 누적시켜 axios를 통해 파이썬으로 보내줌
    .then(res => {
      alert(`회원가입 완료: ${res.data.result}`)
      // history.pushState('login') // 회원가입 후 로그인 페이지로 넘어감
    }) //성공
    .catch(err => {
      alert(`회원가입 실패: ${err}`)
    }) //실패
    
   
    
    

  
  }

  const handleClick = e => {
    e.preventDefault()
    alert('취소 클릭')
  }


    // closer 뭘하든 마지막에 얘가 실행되고, 위에있는 함수 호출
    return (<>       
    <div className="Signup"> 
    <form onSubmit={handleSubmit} method = "post" style={{border:"1px solid #ccc"}}>
      <div className="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr/>

        <label for="username"><b>User ID</b></label>
        <input type="text" placeholder="Enter ID" onChange = {handleChange} name="username" value={username}/>

        <label for="password"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" onChange = {handleChange} name="password" value={password}/>

        <label for="name"><b>Name</b></label>
        <input type="text" placeholder="Enter Your Name" onChange = {handleChange} name="name" value={name}/>

        <label for="email"><b>Email</b></label>
        <input type="text" placeholder="Enter Email" onChange = {handleChange} name="email" value={email}/>

        <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

        <div class="clearfix">
          <button type="submit" className="signupbtn">Sign Up</button>
          <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
      
    </div>
  </div>
</form>
</div>
</>)
}

export default SignUp;