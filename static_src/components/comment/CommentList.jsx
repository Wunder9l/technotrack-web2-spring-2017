import React from 'react';
import PropTypes from 'prop-types';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import Comment from './Comment';
import apiUrls from '../ApiUrls';
import {loadComments} from '../../actions/components/Comment';


class CommentList extends React.Component {

    static propTypes = {
        commentList: PropTypes.arrayOf(PropTypes.shape(Comment.propTypes)).isRequired,
        isLoading: PropTypes.bool.isRequired,
        loadComments: PropTypes.func.isRequired,
    };

    // state = {commentList: [], isLoading};

    componentDidMount() {
        this.props.loadComments(apiUrls.commentList);
    }

    render() {
        if (this.props.isLoading) {
            return <div className="comments-list">Loading...</div>;
        }
        const likeObjects = this.props.commentList.map(
            item => <Comment key={item.id} object={item.object} author={item.author} updated={item.updated}
                             text={item.text}/>
        );
        // console.log(this.state);

        return (

            <div className="comments-list">
                {likeObjects}
            </div>
        );
    }
}


const mapStoreToProps = ({comments}) => {
    return {
        commentList: comments.commentList,
        isLoading: comments.isLoading,
    };
};

const mapDispatchToProps = (dispatch) => {
    return bindActionCreators(loadComments, dispatch);
};

export default connect(mapStoreToProps, mapDispatchToProps)(CommentList);