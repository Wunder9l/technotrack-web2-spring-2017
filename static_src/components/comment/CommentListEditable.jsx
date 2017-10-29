import React from 'react';
import CommentForm from './CommentForm';
import CommentList from './CommentList';
import apiUrls from '../ApiUrls';


class CommentListEditable extends React.Component {

    render() {
        return (
            <div>
                <CommentForm/>
                <p/>
                <CommentList/>
            </div>
        );
    }
}

export default CommentListEditable;