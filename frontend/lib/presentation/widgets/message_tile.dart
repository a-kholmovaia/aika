import 'package:flutter/material.dart';
import 'package:frontend/domain/entities/message.dart';
import 'package:frontend/utils/audio_utils.dart';
import 'package:frontend/presentation/widgets/chat_widgets.dart';
import 'package:frontend/presentation/widgets/audio_player_widget.dart';
import 'package:frontend/styles/app_styles.dart';

class MessageTile extends StatefulWidget {
  final String content;
  final String role;
  final MessageType messageType;
  final String audio;

  const MessageTile({
    required this.content,
    required this.role,
    required this.messageType,
    this.audio = '',
  });

  @override
  _MessageTileState createState() => _MessageTileState();
}

class _MessageTileState extends State<MessageTile> {
  late AudioUtils _audioManager;
  bool _isPlaying = false;

  @override
  void initState() {
    super.initState();
    _audioManager = AudioUtils();
    if (widget.messageType == MessageType.listening) {
      _prepareAudioFile();
    }
  }

  @override
  void dispose() {
    _audioManager.dispose();
    super.dispose();
  }

  Future<void> _prepareAudioFile() async {
    await _audioManager.prepareAudioFile(widget.audio);
    setState(() {});
  }

  void _playPauseAudio() async {
    await _audioManager.playPauseAudio(_isPlaying);
    setState(() {
      _isPlaying = !_isPlaying;
    });
  }

  @override
  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;
    double unitW = screenSize.width * 0.01;
    double unitH = screenSize.height * 0.01;
    bool isBot = widget.role == 'bot';
    double radius = unitW * 2;

    var borderRadius = isBot
        ? BorderRadius.only(
            topLeft: Radius.circular(radius),
            topRight: Radius.circular(radius),
            bottomLeft: const Radius.circular(0),
            bottomRight: Radius.circular(radius),
          )
        : BorderRadius.only(
            topLeft: Radius.circular(radius),
            topRight: Radius.circular(radius),
            bottomLeft: Radius.circular(radius),
            bottomRight: const Radius.circular(0),
          );

    return Column(
      children: [
        Row(
          mainAxisAlignment:
              isBot ? MainAxisAlignment.start : MainAxisAlignment.end,
          crossAxisAlignment: CrossAxisAlignment.end,
          children: [
            if (isBot) BotAvatar(unitW: unitW),
            MessageContent(
              unitW: unitW,
              unitH: unitH,
              screenSize: screenSize,
              borderRadius: borderRadius,
              content: widget.content,
              messageType: widget.messageType,
              isPlaying: _isPlaying,
              playPauseAudio: _playPauseAudio,
              buildAudioWaveform: _buildAudioWaveform,
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildAudioWaveform() {
    return AudioPlayer(
      maxDuration: _audioManager.maxDuration,
      positionStream: _audioManager.positionStream,
      playPauseAudio: _playPauseAudio,
      isPlaying: _isPlaying,
    );
  }
}


class MessageContent extends StatelessWidget {
  const MessageContent({
    Key? key,
    required this.unitW,
    required this.unitH,
    required this.screenSize,
    required this.borderRadius,
    required this.content,
    required this.messageType,
    required this.isPlaying,
    required this.playPauseAudio,
    required this.buildAudioWaveform,
  }) : super(key: key);

  final double unitW;
  final double unitH;
  final Size screenSize;
  final BorderRadius borderRadius;
  final String content;
  final MessageType messageType;
  final bool isPlaying;
  final VoidCallback playPauseAudio;
  final Widget Function() buildAudioWaveform;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(horizontal: unitW, vertical: unitH),
      padding: EdgeInsets.symmetric(horizontal: unitW * 1.5, vertical: unitH),
      constraints: BoxConstraints(maxWidth: screenSize.width * 0.7),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: borderRadius,
        border: Border.all(color: Colors.black, width: 1.5),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            content,
            style: AppStyles.messageTextStyle,
            softWrap: true,
          ),
          if (messageType == MessageType.listening) buildAudioWaveform(),
        ],
      ),
    );
  }
}