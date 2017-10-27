import React from 'react';
import PropTypes from 'prop-types';

class Like extends React.Component {
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
    };
    static defaultProps = {};

    render() {
        return (
            <div className="like-item">
                <div className="like-item-author">
                    <b>Author: {this.props.author.username}, </b>
                </div>
                <div className="event-item-title">
                    <i>{this.props.updated}</i>
                </div>
                <div>
                    <p>
                        Object: {this.props.object.title}
                    </p>
                </div>
            </div>
        );
    }
}

export default Like;