import React,{useState} from 'react'
import 'member/styles/MemberDetail.css'
import { memberModify } from 'api'
import { useHistory } from 'react-router';
import { Link } from 'react-router-dom';

const MemberModifyForm = () => {
    const history = useHistory()
    const [changedPassword, setChangedPassword] = useState('')


    const handleSubmit = e => {
      e.preventDefault()
      const member = JSON.parse(localStorage.getItem("loginedMember"))
      
      alert(changedPassword)
      member.password = changedPassword
      alert(JSON.stringify(member))
      
      memberModify({member})
      .then(res => {
        alert(`비밀번호 수정 완료 : ${res.data.result} `)
        localStorage.setItem("loginedMember","")
        history.push('member-login')
        
      })
      .catch(err => {
        alert(`비밀번호 수정 실패 : ${err} `)
  
      })
    }
    // method가 put인 것이 중요
    return (<>
    <form method="put" onSubmit={handleSubmit} >
            
                <h2 style={{"text-align":"center"}}>비밀번호 수정</h2>
        <div className="container">
          <label labelFor="psw"><b>변경할 비밀번호</b></label>
          <input type="password" placeholder="Enter Password" onChange={e => {setChangedPassword(e.target.value)}} name="password" required/>
              
          <button type="submit">확 인</button>
         
        </div>

      </form>

       
      </>)
}

export default MemberModifyForm