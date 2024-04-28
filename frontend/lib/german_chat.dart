import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart' as intl;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart' as shared_preferences;
import 'package:uuid/uuid.dart' as uuid;
import 'message.dart';
import 'ui_elements.dart';

class GermanChatPage extends StatefulWidget {
  @override
  _GermanChatState createState() => _GermanChatState();

}

class _GermanChatState extends State {
  final TextEditingController _controller = TextEditingController();
  List<Message> _messages = [];
  late String _userId;

  @override
  void initState() {
    super.initState();
    _initUserId();
  }

  Future<void> _initUserId() async {
    final prefs = await shared_preferences.SharedPreferences.getInstance();
    final userId = prefs.getString('userId');
    if (userId != null) {
      setState(() {
        _userId = userId;
      });
    } else {
      final newUserId = const uuid.Uuid().v4(); // Generate new UUID
      await prefs.setString('userId', newUserId); // Save userID in SharedPreferences
      setState(() {
        _userId = newUserId;
      });
    }
  }

  String generateMessageID() {
    return uuid.Uuid().v4();
  }

  Message _addMessage(String text, String role) {
    String timestamp = getCurrenTimestamp();
    String messageID = generateMessageID();
    return Message(text: text, userID: _userId, 
                  messageID: messageID, role: role, 
                  timestamp: timestamp);

  }
  
  String getCurrenTimestamp() {
    return intl.DateFormat('yyyy-MM-dd HH:mm:ss').format(DateTime.now());
  }

  Map<String, dynamic> getMessageBodyHTTP(Message message) {
  // Construct message body with userId, role, and timestamp
    return  {
      'message': message.getText(),
      'userId': message.getUserID(),
      'messageId': message.getMessageID(),
      'role': message.getRole(),
      'timestamp':message.getTimestamp(),
    };
  }

  Future<void> _handleSubmitted(String text) async {
    if (text == '') return;
    _controller.clear();
    
    Message userMessage = Message(text: text, userID: _userId, 
                          messageID: generateMessageID(), 
                          role: 'user', 
                          timestamp: getCurrenTimestamp());


    Message botMessage = Message(text: "Echo: $text", userID: _userId, 
                          messageID: generateMessageID(), 
                          role: 'bot', 
                          timestamp: getCurrenTimestamp());

    botMessage.displayMessage();
    setState(() {
      _messages.add(userMessage);
      _messages.add(botMessage);
    });
/*
    // Send message to backend
    messageBody = getMessageBodyHTTP(userMessage);
    final response = await http.post(
      Uri.parse('https://your-backend-api.com/messages'), // Replace with your backend API URL
      body: messageBody,
    );
    if (response.statusCode == 200) {
      // Decode response JSON
      final responseData = jsonDecode(response.body);
      // Check if response contains a message
      if (responseData.containsKey('message')) {
        Message botMessage = Message(text: responseData['message'], userID: _userId, 
                          messageID: generateMessageID(), 
                          role: 'bot', 
                          timestamp: getCurrenTimestamp());
        setState(() {
          _messages.add(botMessage);
        });
      }
    } else {
      // Handle error
    }
*/
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appBarAIKA(context),
      body: Column(
        children: <Widget>[
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(8),
              reverse: true,
              itemBuilder: (_, int index) => _buildMessageTile(_messages.reversed.toList()[index], context),
                itemCount: _messages.length,
              ),
          ),
          const Divider(height: 1),
          _buildTextInput(_controller, _handleSubmitted)
        ],
      ),
    );
  }
}

Widget _buildMessageTile(Message message, BuildContext context) {
  bool isBot = message.text.startsWith('Echo');
  const double radius = 6;
  var borderRadius = isBot 
          ? const BorderRadius.only(
            topLeft: Radius.circular(radius), 
            topRight: Radius.circular(radius),
            bottomLeft: Radius.circular(0),
            bottomRight: Radius.circular(radius)
          )
          : const BorderRadius.only(
            topLeft: Radius.circular(radius), 
            topRight: Radius.circular(radius),
            bottomLeft: Radius.circular(radius),
            bottomRight: Radius.circular(0)
          );
          
  return Row(
    mainAxisAlignment: isBot? MainAxisAlignment.start : MainAxisAlignment.end,
    children: [
      if (isBot)
        const CircleAvatar(
          child:  Text('B'),
          backgroundColor: Colors.orange,
          foregroundColor: Colors.grey,
          ),
      Container(
        margin: const EdgeInsets.symmetric( horizontal: 8, vertical: 10),
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
        constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.7),
        decoration: BoxDecoration(
          color: isBot ? Colors.orange : Colors.grey,
          borderRadius: borderRadius,
        ),
        child: Text(message.text),
      ),
      if (!isBot)
        const CircleAvatar(
          child:  Text('U'),
          backgroundColor: Colors.grey,
          foregroundColor: Colors.orange,
          ),
    ],
    );
}
  

Widget _buildTextInput(_controller, _handleSubmitted) {
  return Padding(
            padding: const EdgeInsets.all(8),
            child: Container(
              decoration: BoxDecoration( 
                border: Border.all(color: Colors.black),
                borderRadius: BorderRadius.circular(5),
              ),
              child: Row(
                children: <Widget>[
                  Expanded(
                    child: Padding(
                        padding: EdgeInsets.only(left:10),
                        child:TextField(
                          controller: _controller,
                          keyboardType: TextInputType.multiline,
                          maxLines: 7,
                          minLines: 1,
                          onSubmitted: _handleSubmitted,
                          decoration: const InputDecoration.collapsed(hintText: '  Tippen Sie hier...'),
                        ),
                      ),
                    ),
                  IconButton(
                    onPressed:() => _handleSubmitted(_controller.text), 
                    icon: const Icon(Icons.send))
                ],
      )
    )
  );
}

