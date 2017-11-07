import React from 'react';
import PropTypes from 'prop-types';
import {bindActionCreators} from 'redux';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import {connect} from 'react-redux';
import apiUrls from '../ApiUrls';
import {addComment} from '../../actions/components/CommentAction';
import {getCsrfToken} from '../../utils/Helpers';

class CommentForm extends React.Component {
    static propTypes = {
        contentType: PropTypes.number.isRequired,
        objectId: PropTypes.number.isRequired,
        addComment: PropTypes.func.isRequired,
    };
    state = {
        text: '',
        errorText: '',
    };

    onChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value,
            errorText: '',
        });
    };

    clearForm = () => {
        this.setState({
            text: '',
            errorText: '',
        });
    }

    onSubmit = (e) => {
        e.preventDefault();
        // console.log(JSON.stringify(this.state));
        const jsonBody = JSON.stringify(Object.assign({}, {
            content_type: String(this.props.contentType),
            object_id: String(this.props.objectId),
        }, this.state));
        console.log('JSON', jsonBody);
        fetch(apiUrls.commentList, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            method: 'POST',
            credentials: 'include',
            body: jsonBody,
            // body: JSON.stringify(this.state),
        }).then(
            (result) => {
                if (result.ok) {
                    result.json().then(
                        (json) => {
                            this.props.addComment(json);
                            this.clearForm();
                        });
                } else {
                    throw result;
                }
            }
        ).catch(
            (error) => {
                return error.json().then(
                    (json) => {
                        const errMsg = Object.entries(json).map(([key, value]) => {
                            return (`${key}: ${value}`);
                        })
                            .reduce((prev, curr) => `${prev}\r\n${curr}`);
                        this.setState({errorText: errMsg});
                    }
                )
            }
        )
    };

    isSubmitEnabled = () => {
        return this.state.text.length === 0;
    };

    render() {
        return (
            <div className="comment-create-form" data-background-color="333333">
                <form>
                    <div className="comment-form-text">
                        <TextField
                            hintText="Enter comment text"
                            multiLine={true}
                            rows={2}
                            rowsMax={4}
                            name="text" onChange={this.onChange} value={this.state.text}
                            errorText={this.state.errorText}
                        />
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


const mapStoreToProps = (store, ownProps) => {
    // const comments = store.get('comments');
    return {
        contentType: ownProps.contentType,
        objectId: ownProps.objectId,
    };
};

const mapDispatchToProps = (dispatch) => {
    // return {};
    return bindActionCreators({addComment}, dispatch);
};

export default connect(mapStoreToProps, mapDispatchToProps)(CommentForm);