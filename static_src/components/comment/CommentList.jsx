import React from 'react';
import PropTypes from 'prop-types';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import Comment from './Comment';
import apiUrls from '../ApiUrls';
import {loadComments} from '../../actions/components/CommentAction';
import {List, ListItem} from 'material-ui/List';
import Subheader from 'material-ui/Subheader'


class CommentList extends React.Component {

    static propTypes = {
        contentType: PropTypes.number,
        objectId: PropTypes.number,
        commentList: PropTypes.object.isRequired,
        isLoading: PropTypes.bool.isRequired,
        loadComments: PropTypes.func.isRequired,
    };

    // state = {commentList: [], isLoading};

    componentDidMount() {
        if (this.props.contentType && this.props.objectId) {
            const params = `?object_id=${this.props.objectId}&content_type=${this.props.contentType}`;
            this.props.loadComments(apiUrls.commentList + params);
        } else {
            this.props.loadComments(apiUrls.commentList);
        }
    }

    render() {
        if (this.props.isLoading) {
            return <div className="comments-list">Loading...</div>;
        }
        const comments = Array();
        this.props.commentList.forEach(
            item => comments.push(<Comment key={item.id} {...item} />)
        );
        // debugger;
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


const mapStoreToProps = (store, ownProps) => {
    const comments = store.get('comments');
    // console.log("CommentList", comments);
    return {
        commentList: comments.get('commentList'),
        isLoading: comments.get('isLoading'),
        contentType: ownProps.contentType,
        objectId: ownProps.objectId,
    };
};

const mapDispatchToProps = (dispatch) => {
    // return {};
    return bindActionCreators({loadComments}, dispatch);
};

export default connect(mapStoreToProps, mapDispatchToProps)(CommentList);