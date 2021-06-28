import React from 'react'
import { Link } from 'react-router-dom'

export const UserMenu = () => (<nav>
        <ol>
            <li><Link to='/signup-form'>회원가입</Link></li>
            <li><Link to='/login'>로그인</Link></li>
            <li><Link to='/user-detail'>회원정보상세</Link></li>
            <li><Link to='/user-modify'>회원정보수정</Link></li>
            <li><Link to='/user-remove'>회원정보삭제</Link></li>
        </ol>
</nav>

)
export const ItemMenu = () => (<nav>
    <ol>
        <li><Link to='/item-list'>아이템 목록</Link></li>
        <li><Link to='/item-register'>아이템 등록</Link></li>
        <li><Link to='/item-detail'>아이템 상세</Link></li>
        <li><Link to='/item-remove'>아이템 삭제</Link></li>
    </ol>
</nav>


)
export const BlogMenu = () => (<nav>
    <ol>
        <li><Link to='/post-list'>게시글 목록</Link></li>
        <li><Link to='/post-register'>게시글 쓰기</Link></li>
        <li><Link to='/post-retrive'>게시글 조회</Link></li>
        <li><Link to='/post-update'>게시글 수정</Link></li>
        <li><Link to='/post-delete'>회원정보삭제</Link></li>
    </ol>
</nav>
)

export const StockMenu = () => (<nav>
    <ol>
        <li><Link to='/stock-list'>게시글 목록</Link></li>
        <li><Link to='/stock-write'>게시글 쓰기</Link></li>
        <li><Link to='/stock-read'>게시글 읽기</Link></li>
        <li><Link to='/stock-read'>회원정보삭제</Link></li>
    </ol>
</nav>

)