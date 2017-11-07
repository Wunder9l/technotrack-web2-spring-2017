import React from 'react';
import PropTypes from 'prop-types';

import CommentForm from './CommentForm';
import CommentList from './CommentList';
import apiUrls from '../ApiUrls';


class CommentListEditable extends React.Component {

    static propTypes = {
        contentType: PropTypes.number,
        objectId: PropTypes.number,
    };

    render() {
        return (
            <div>
                <CommentForm contentType={this.props.contentType} objectId={this.props.objectId}/>
                <p/>
                <CommentList contentType={this.props.contentType} objectId={this.props.objectId}/>
            </div>
        );
    }
}

export default CommentListEditable;