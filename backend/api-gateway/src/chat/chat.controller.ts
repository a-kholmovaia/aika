import { Controller, Post, Get, Body } from '@nestjs/common';
import { ChatService } from './chat.service';
import { Message } from './models/message.dto';
import { ApiTags, ApiResponse, ApiExtraModels, getSchemaPath } from '@nestjs/swagger';

/**
 * Controller class for handling POST requests for processing messages in a
German chat application.
 * @class GermanChatController
 */
@ApiTags('API-Gateway')
@Controller('chat')
export class ChatController {
  constructor(private readonly germanChatService: ChatService) {}

  @ApiExtraModels(Message)
  @ApiResponse({
     status: 201,
     schema: {
       $ref: getSchemaPath(Message),
     },
   })

  @Post('german')
  async getAnswer( @Body() userMessage: Message, ): 
    Promise<{ message: Message }> {
    console.log('german');
    const message = await this.germanChatService.processMessage(userMessage, "language");
    return { message };
  }

  @Post('law')
  async getAnswerLawLife( @Body() userMessage: Message, ): 
    Promise<{ message: Message }> {
    console.log('law');
    const message = await this.germanChatService.processMessage(userMessage, "law-life");
    return { message };
  }

  @Get('lesson')
  async getLesson( @Body() userMessage: Message): 
    Promise<JSON> {
    console.log('lesson');
    const lesson = await this.germanChatService.get_lesson("[Grammar][Futur I][None][3][2][1]")
    return lesson;
  }
}
