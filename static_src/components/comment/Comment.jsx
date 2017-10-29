import React from 'react';
import PropTypes from 'prop-types';
import {ListItem} from 'material-ui/List';
import Divider from 'material-ui/Divider';

class Comment extends React.Component {
    static propTypes = {
        id: PropTypes.number.isRequired,
        object_id: PropTypes.number.isRequired,
        content_type: PropTypes.number.isRequired,
        author: PropTypes.number,
        author_name: PropTypes.string.isRequired,
        text: PropTypes.string.isRequired,
        updated: PropTypes.string.isRequired,
    };
    static
    defaultProps = {};

    render() {
        return (
            < ListItem primaryText={<p>{this.props.author_name}, {this.props.updated}</p>}
                       secondaryText={<p>{this.props.text}</p>} secondaryTextLines={2}>
                <Divider/>
            </ListItem>
        );
    }
}

export default Comment;