import React from 'react';
import PropTypes from 'prop-types';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import apiUrls from '../ApiUrls';
import {loadPost} from '../../actions/components/PostAction';
import CommentListEditable from '../comment/CommentListEditable';


class Post extends React.Component {
    static postObjectShape = {
        id: PropTypes.number.isRequired,
        author: PropTypes.number.isRequired,
        author_username: PropTypes.string.isRequired,
        likes: PropTypes.arrayOf(PropTypes.number).isRequired,
        created: PropTypes.string.isRequired,
        updated: PropTypes.string.isRequired,
        likes_count: PropTypes.number.isRequired,
        comments_count: PropTypes.number.isRequired,
        title: PropTypes.string.isRequired,
        title_image: PropTypes.string.isRequired,
    };

    static propTypes = {
        id: PropTypes.number.isRequired,
        postObject: PropTypes.object,
        isLoaded: PropTypes.bool.isRequired,
        loadPost: PropTypes.func.isRequired,
    };

    postContentType = 11;

    componentDidMount() {
        if (!this.props.postObject) {
            const url = apiUrls.postList + String(this.props.id) + '/';
            console.log('LoadPost', url);
            this.props.loadPost(url);
        }
    }

    render() {
        if (this.props.isLoaded) {
            // debugger;
            let imgSrc = this.props.postObject.title_image;
            imgSrc = 'http://localhost/' + imgSrc.substr(imgSrc.search('/media') + 1);
            return (
                <div className='post-with-comment'>
                    <Card>
                        <CardHeader
                            title={this.props.postObject.author_username}
                            // subtitle={this.props.updated}
                            // avatar="images/jsa-128.jpg"
                        />
                        <CardMedia
                            overlay={
                                <CardTitle title={this.props.postObject.title}
                                           subtitle={this.props.postObject.updated}/>
                            }
                        >
                            <img src={imgSrc} alt=""/>
                        </CardMedia>
                        {/*<CardTitle title={this.props.postObject.title} subtitle={this.props.postObject.updated}/>*/}
                    </Card>
                    <CommentListEditable contentType={this.postContentType} objectId={this.props.postObject.id}/>
                </div>
            );

            // return <div>Nothing</div>;
        } else {
            return <div className="comments-list">Loading...</div>;
        }
    }
}

const mapStoreToProps = (store, ownProps) => {
    const posts = store.get('posts');
    console.log('Post', posts);
    // debugger;
    if (posts.getIn(['postList', String(ownProps.id)])) {
        return {
            id: ownProps.id,
            postObject: posts.getIn(['postList', String(ownProps.id)]),
            isLoaded: true,
        };
    }
    return {
        id: ownProps.id,
        isLoaded: false,
    };
};
//
const mapDispatchToProps = (dispatch) => {
    // return {};
    return bindActionCreators({loadPost}, dispatch);
};
//
export default connect(mapStoreToProps, mapDispatchToProps)(Post);