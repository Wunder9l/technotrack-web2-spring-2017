import React from 'react';
import PropTypes from 'prop-types';
import {bindActionCreators} from 'redux';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import {connect} from 'react-redux';
import apiUrls from '../ApiUrls';
import {addComment} from '../../actions/components/Comment';
import {getCsrfToken} from '../../utils/Helpers';

class CommentForm extends React.Component {
    state = {
        text: '',
        content_type: '',
        object_id: '',

    };
    static propTypes = {
        addComment: PropTypes.func.isRequired,
    };

    onChange = (e) => {
        this.setState({[e.target.name]: e.target.value});
    };

    clearForm = () => {
        this.setState({
            text: '',
            content_type: '',
            object_id: '',
        });
    }

    onSubmit = (e) => {
        e.preventDefault();
        // console.log(JSON.stringify(this.state));
        // console.log(apiUrls.commentList);
        fetch(apiUrls.commentList, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(this.state),
        }).then(
            body => body.json(),
        ).then(
            (json) => {
                this.props.addComment(json);
                this.clearForm();
            });
    };

    isSubmitEnabled = () => {
        return this.state.text.length === 0;
    };

    render() {
        return (
            <div className="comment-create-form" data-background-color="333333">
                <form>
                    {/*<DjangoCSRFToken className="comment-form-object-type"/>*/}
                    <div className="comment-form-object-type">
                        <i>Content type:</i>
                        <input name="content_type" onChange={this.onChange} type="number"
                               value={this.state.content_type}/>
                    </div>
                    <div className="comment-form-object-type">
                        <i>Object id:</i>
                        <input name="object_id" onChange={this.onChange} type="number" value={this.state.object_id}/>
                    </div>
                    <div className="comment-form-text">
                        <TextField
                            hintText="Enter comment text"
                            multiLine={true}
                            rows={2}
                            rowsMax={4}
                            name="text" onChange={this.onChange} value={this.state.text}
                        />
                        {/*<i>Text:</i>*/}
                        {/*<textarea/>*/}
                    </div>
                    <div className="comment-form-submit">
                        <RaisedButton disabled={this.isSubmitEnabled()} label="Submit" primary={true}
                                      onClick={this.onSubmit}/>
                    </div>
                </form>
            </div>
        );
    }
}


const mapStoreToProps = (store) => {
    // const comments = store.get('comments');
    return {
        // commentList: comments.get('commentList'),
        // isLoading: comments.get('isLoading'),
    };
};

const mapDispatchToProps = (dispatch) => {
    // return {};
    return bindActionCreators({addComment}, dispatch);
};

export default connect(mapStoreToProps, mapDispatchToProps)(CommentForm);