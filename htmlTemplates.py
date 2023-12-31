css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://images.pexels.com/photos/16103245/pexels-photo-16103245/free-photo-of-cute-android-walking-in-front-of-a-graffiti-wall.jpeg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://images.pexels.com/photos/2761017/pexels-photo-2761017.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''