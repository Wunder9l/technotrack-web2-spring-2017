import React from 'react';
import CommentForm from './CommentForm';
import CommentList from './CommentList';
import apiUrls from '../ApiUrls';


class CommentListEditable extends React.Component {

    state = {commentList: [], isLoading: true};

    //
    componentDidMount() {
        fetch(apiUrls.commentList, {credentials: 'include'}
        ).then(
            (body) => body.json(),
        ).then(
            (json) => this.setState({commentList: json, isLoading: false}),
            // (json) => console.log(json),
        );
    }

    onCommentCreate = (comment) => {
        this.setState({
            commentList: [comment, ...this.state.commentList],
        });
    }

    render() {
        return (
            <div>
                <CommentForm onCreate={this.onCommentCreate}/>
                <p>
                    <CommentList isLoading={this.state.isLoading} commentList={this.state.commentList}/>
                </p>
            </div>
        );
    }
}

export default CommentListEditable;