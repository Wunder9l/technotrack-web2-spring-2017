import React from 'react';
import PropTypes from 'prop-types';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import Comment from './Comment';
import apiUrls from '../ApiUrls';
import {loadComments} from '../../actions/components/Comment';
import {List, ListItem} from 'material-ui/List';
import Subheader from 'material-ui/Subheader'


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
        const comments = this.props.commentList.map(
            item => <Comment key={item.id} {...item} />
        );

        return (

            <div className="event-list">
                <List>
                    <Subheader>Comments</Subheader>
                    {comments}
                </List>
            </div>
        );
        // return <div>Nothing</div>;
    }
}


const mapStoreToProps = (store) => {
    // console.log("STORE!!!",store);
    const comments = store.get('comments');
    // console.log('comments', comments);
    //
    return {
        commentList: comments.get('commentList'),
        isLoading: comments.get('isLoading'),
    };
};

const mapDispatchToProps = (dispatch) => {
    // return {};
    return bindActionCreators({loadComments}, dispatch);
};

export default connect(mapStoreToProps, mapDispatchToProps)(CommentList);