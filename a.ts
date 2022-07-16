/**
 * Complete the hackathon before your opponent by following the principles of Green IT
 **/


// game loop
class Player {
    constructor(
        public location: number,
        public score: number,
        public permanentDailyRoutineCards: number,
        public permanentArchitectureStudyCards: number,
        public cards: Card[],

    ) { }
}
enum Card {
    TRAINING,
    CODING,
    DAILY_ROUTINE,
    TASK_PRIORITIZATION,
    ARCHITECTURE_STUDY,
    CONTINUOUS_DELIVERY,
    CODE_REVIEW,
    REFACTORING,
    BONUS,
    TECHNICAL_DEBT
}

class Application {
    constructor(
        public objectType: string,
        public id: number,
        public trainingNeeded: number,
        public codingNeeded: number,
        public dailyRoutineNeeded: number,
        public taskPrioritizationNeeded: number,
        public architectureStudyNeeded: number,
        public continuousDeliveryNeeded: number,
        public codeReviewNeeded: number,
        public refactoringNeeded: number
    ) { }
} 
let player : Player = new Player(0, 0, 0, 0, []);
let enemy : Player = new Player(0, 0, 0, 0, []);
let applications : Application[] = [];

while (true) {
    const gamePhase: string = readline(); // can be MOVE, GIVE_CARD, THROW_CARD, PLAY_CARD or RELEASE
    const applicationsCount: number = parseInt(readline());
    // for (let i = 0; i < applicationsCount; i++) {
    //     var inputs: string[] = readline().split(' ');
    //     const objectType: string = inputs[0];
    //     const id: number = parseInt(inputs[1]);
    //     const trainingNeeded: number = parseInt(inputs[2]); // number of TRAINING skills needed to release this application
    //     const codingNeeded: number = parseInt(inputs[3]); // number of CODING skills needed to release this application
    //     const dailyRoutineNeeded: number = parseInt(inputs[4]); // number of DAILY_ROUTINE skills needed to release this application
    //     const taskPrioritizationNeeded: number = parseInt(inputs[5]); // number of TASK_PRIORITIZATION skills needed to release this application
    //     const architectureStudyNeeded: number = parseInt(inputs[6]); // number of ARCHITECTURE_STUDY skills needed to release this application
    //     const continuousDeliveryNeeded: number = parseInt(inputs[7]); // number of CONTINUOUS_DELIVERY skills needed to release this application
    //     const codeReviewNeeded: number = parseInt(inputs[8]); // number of CODE_REVIEW skills needed to release this application
    //     const refactoringNeeded: number = parseInt(inputs[9]); // number of REFACTORING skills needed to release this application
    // }
    for (let i = 0; i < applicationsCount; i++) {
        var inputs: string[] = readline().split(' ');
        applications.push(new Application(inputs[0], parseInt(inputs[1]), parseInt(inputs[2]), parseInt(inputs[3]), parseInt(inputs[4]), parseInt(inputs[5]), parseInt(inputs[6]), parseInt(inputs[7]), parseInt(inputs[8]), parseInt(inputs[9])));
    }
    
        // for (let i = 0; i < 2; i++) {
    //     var inputs: string[] = readline().split(' ');
    //     const playerLocation: number = parseInt(inputs[0]); // id of the zone in which the player is located
    //     const playerScore: number = parseInt(inputs[1]);
    //     const playerPermanentDailyRoutineCards: number = parseInt(inputs[2]); // number of DAILY_ROUTINE the player has played. It allows them to take cards from the adjacent zones
    //     const playerPermanentArchitectureStudyCards: number = parseInt(inputs[3]); // number of ARCHITECTURE_STUDY the player has played. It allows them to draw more cards
    // }
    var inputs: string[] = readline().split(' ');
    player.location =  parseInt(inputs[0]); // id of the zone in which the player is located
    player.score = parseInt(inputs[1]);
    player.permanentDailyRoutineCards = parseInt(inputs[2]); // number of DAILY_ROUTINE the player has played. It allows them to take cards from the adjacent zones
    player.permanentArchitectureStudyCards = parseInt(inputs[3]); // number of ARCHITECTURE_STUDY the player has played. It allows them to draw more cards
    inputs = readline().split(' ');
    enemy.location = parseInt(inputs[0]); // id of the zone in which the player is located
    enemy.score =  parseInt(inputs[1]);
    enemy.permanentDailyRoutineCards = parseInt(inputs[2]); // number of DAILY_ROUTINE the player has played. It allows them to take cards from the adjacent zones
    enemy.permanentArchitectureStudyCards = parseInt(inputs[3]); // number of ARCHITECTURE_STUDY the player has played. It allows them to draw more cards
    
    const cardLocationsCount: number = parseInt(readline());
    for (let i = 0; i < cardLocationsCount; i++) {
        var inputs: string[] = readline().split(' ');
        const cardsLocation: string = inputs[0]; // the location of the card list. It can be HAND, DRAW, DISCARD or OPPONENT_CARDS (AUTOMATED and OPPONENT_AUTOMATED will appear in later leagues)
        const trainingCardsCount: number = parseInt(inputs[1]);
        const codingCardsCount: number = parseInt(inputs[2]);
        const dailyRoutineCardsCount: number = parseInt(inputs[3]);
        const taskPrioritizationCardsCount: number = parseInt(inputs[4]);
        const architectureStudyCardsCount: number = parseInt(inputs[5]);
        const continuousDeliveryCardsCount: number = parseInt(inputs[6]);
        const codeReviewCardsCount: number = parseInt(inputs[7]);
        const refactoringCardsCount: number = parseInt(inputs[8]);
        const bonusCardsCount: number = parseInt(inputs[9]);
        const technicalDebtCardsCount: number = parseInt(inputs[10]);
    }
    const possibleMovesCount: number = parseInt(readline());
    for (let i = 0; i < possibleMovesCount; i++) {
        const possibleMove: string = readline();
    }


    // Write an action using console.log()
    // To debug: console.error('Debug messages...');


    // In the first league: RANDOM | MOVE <zoneId> | RELEASE <applicationId> | WAIT; In later leagues: | GIVE <cardType> | THROW <cardType> | TRAINING | CODING | DAILY_ROUTINE | TASK_PRIORITIZATION <cardTypeToThrow> <cardTypeToTake> | ARCHITECTURE_STUDY | CONTINUOUS_DELIVERY <cardTypeToAutomate> | CODE_REVIEW | REFACTORING;
    console.log('RANDOM');
}


