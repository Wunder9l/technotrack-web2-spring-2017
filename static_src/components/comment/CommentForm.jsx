import React from 'react';
import PropTypes from 'prop-types';
import DjangoCSRFToken from '../DjangoCSRFToken';
// import DjangoCSRFToken from 'django-react-csrftoken';
import apiUrls from '../ApiUrls';

class CommentForm extends React.Component {
    state = {
        text: '',
        content_type: '',
        object_id: '',
    };

    onChange = (e) => {
        this.setState({[e.target.name]: e.target.value});
    };

    onSubmit = (e) => {
        // const csrftoken = Cookies.get('csrftoken');
        e.preventDefault();
        console.log(JSON.stringify(this.state));
        console.log(apiUrls.commentList);
        fetch(apiUrls.commentList, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.cookie.match(/csrftoken=([^ ;]+)/)[1],
                // 'X-Requested-With': 'XMLHttpRequest'
            },
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(this.state),
        }).then(
            body => body.json(),
        ).then(
            (json) => {
                // console.log(e);
                // console.log(json);
                this.props.onCreate(json);
            });
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
                        <i>Text:</i>
                        <textarea name="text" onChange={this.onChange} value={this.state.text}/>
                    </div>
                    <div className="comment-form-submit">
                        <button onClick={this.onSubmit}>Submit</button>
                    </div>
                </form>
            </div>
        );
    }
}

export default CommentForm;