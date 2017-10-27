import React from 'react';
import PropTypes from 'prop-types';

class Comment extends React.Component {
    static propTypes = {
        object: PropTypes.shape({
            id: PropTypes.number,
            title: PropTypes.string,
        }).isRequired,
        author: PropTypes.shape({
            id: PropTypes.number,
            username: PropTypes.string,
        }).isRequired,
        updated: PropTypes.string.isRequired,
        text: PropTypes.string.isRequired,
    };
    static defaultProps = {};

    render() {
        return (
            <div className="comment-item">
                <div className="comment-item-author">
                    <b>Author: {this.props.author.username}, </b>
                </div>
                <div className="comment-item-updated-date">
                    <i>{this.props.updated}</i>
                </div>
                <div className="comment-item-object">
                    Object: {this.props.object.title}
                </div>
                <div className="comment-item-text">
                    <p><i>{this.props.text}</i></p>
                </div>
            </div>
        );
    }
}

export default Comment;