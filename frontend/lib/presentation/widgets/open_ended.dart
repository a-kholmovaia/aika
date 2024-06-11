import 'package:flutter/material.dart';
import 'package:frontend/domain/entities/task.dart';
import 'package:frontend/presentation/widgets/multiple_choice.dart';
import 'package:frontend/styles/app_styles.dart';
class OpenQuestionTask extends StatelessWidget {
  final Task task;

  OpenQuestionTask({required this.task});

  @override
  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;
    double unitW = screenSize.width * 0.01;
    double unitH = screenSize.height * 0.01;
    return Scaffold(
      backgroundColor: AppStyles.sandColor,
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.all(unitW*5),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              TaskQuestionText(task.question),
              SizedBox(height: unitH*3),
              Container(
                decoration: const BoxDecoration(color: Colors.white),
                child: OpenQuestionInput(task),
              ),
              SizedBox(height: unitH),
            ],
          ),
        ),
      ),
    );
  }
}

class OpenQuestionInput extends StatefulWidget {
  Task task;

  OpenQuestionInput(this.task);
  
  @override
  _OpenQuestionInputState createState() => _OpenQuestionInputState();
}

class _OpenQuestionInputState extends State<OpenQuestionInput> {
  final TextEditingController openQuestionController = TextEditingController();

  @override
  void initState() {
    super.initState();
    openQuestionController.text = widget.task.userAnswers.isNotEmpty ? widget.task.userAnswers[0] : '';
  }

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: openQuestionController,
      decoration: const InputDecoration(
        border: OutlineInputBorder(),
        hintText: 'Type your answer here...',
      ),
      maxLines: 3,
      onChanged: (value) {
        setState(() {
          widget.task.userAnswers = [value];
          widget.task.completed = value.isNotEmpty;
        });
      },
    );
  }

  @override
  void dispose() {
    openQuestionController.dispose();
    super.dispose();
  }
}
