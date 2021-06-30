import React , { useState } from 'react'
import './Postwrite.css'
import { useHistory } from 'react-router'
import { userSignup, userLogin, blogpostWrite } from 'api/index'

const PostWrite = () => {
  const [post, setPost] = useState({
      title: '',
      content: ''
  
  })
  
  const {title, content} = post // Json 객체 만들기

  const handleChange = e => {
      const { name, value } = e.target
      setPost({
          ...post, [name]: value
      }) // 입력되는 값은 Json -> {} 키와 밸류를 name과 value로 추가(밑에 있는 것)
  }

  const handleSubmit = e => {
      e.preventDefault()
      alert(`Post: ${JSON.stringify({...post})}`)
      blogpostWrite({...post})
      .then(res => {
          alert(`Post Complete!: ${res.data.result}`)
      })
      .catch(err => {
          alert(`Post Failed!: ${err}`)
      })
  }
    

  const handleClick = e => {
      e.preventDefault()
      alert('cancled!')
       
  }
 


    return (<>       
    <div className="PostWrite"> 
    <form onSubmit={handleSubmit} method = "post" style={{border:"1px solid #ccc"}}>
      <div className="container">
        <h1>게시글 쓰기</h1>
        <p>Please fill in this form to create an account.</p>
        <hr/>

        <label for="title"><b>Title</b></label>
        <input type="text" placeholder="Enter title" onChange = {handleChange} name="title" value={title}/>      

        <label for="content"><b>Content</b></label>
        <input type="content" placeholder="Enter Content" onChange = {handleChange} name="content" value={content}/>

        <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

        <div class="clearfix">
          <button type="submit" className="signupbtn">Post</button>
          <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
      
    </div>
  </div>
</form>
</div>
</>)
}

export default PostWrite;