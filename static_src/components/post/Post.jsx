import React from 'react';
import PropTypes from 'prop-types';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import apiUrls from '../ApiUrls';
import {loadPost} from '../../actions/components/Post';


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
        isLoading: PropTypes.bool.isRequired,
        id: PropTypes.number.isRequired,
        post_object: PropTypes.shape({
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
        }),
    };

    componentDidMount() {
        const url = apiUrls.postList + String(this.props.id);
        console.log('LoadPost', url);
        if (this.props.isLoading) {
            console.log('LoadPost', url);
            this.props.loadPost(url);
        }
    }

    render() {
        if (this.props.isLoading) {
            return <div className="comments-list">Loading...</div>;
        }

        const imgSrc = this.props.post_object.title_image.substr(this.props.post_object.title_image.search('/media') + 1);
        return (

            <Card>
                <CardHeader
                    title={this.props.post_object.author_username}
                    // subtitle={this.props.updated}
                    // avatar="images/jsa-128.jpg"
                />
                <CardMedia
                    overlay={<CardTitle title="Overlay title" subtitle="Overlay subtitle"/>}
                >
                    <img src={imgSrc} alt=""/>
                </CardMedia>
                <CardTitle title={this.props.post_object.title} subtitle={this.props.post_object.updated}/>
            </Card>
        );

        // return <div>Nothing</div>;
    }
}

const mapStoreToProps = (store, ownProps) => {
    // const comments = store.get('comments');
    console.log('Post', store);
    if ('posts' in store) {
        const {posts} = store;
        if (ownProps.id in posts) {
            return {
                id: ownProps.id,
                isLoading: false,
                post_object: posts[ownProps.id],
            };
        }
    }
    return {
        commentList: ownProps.id,
        isLoading: true,
    };
};
//
const mapDispatchToProps = (dispatch) => {
    // return {};
    return bindActionCreators({loadPost}, dispatch);
};
//
export default connect(mapStoreToProps, mapDispatchToProps)(Post);