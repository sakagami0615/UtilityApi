function [tetrisParam] = TEST_SAMPLE()

% �u���b�N�̃T�C�Y
blockSize = 35;

% �u���b�N�̐F
blockColor = table([],[], 'VariableNames',{'ColorName', 'ColorValue'});
blockColor = vertcat(blockColor, {'LightBlue', {[0.0, 1.0, 1.0]}});
blockColor = vertcat(blockColor, {'Yellow',    {[1.0, 1.0, 0.0]}});
blockColor = vertcat(blockColor, {'Green',     {[0.0, 1.0, 0.0]}});
blockColor = vertcat(blockColor, {'Red',       {[1.0, 0.0, 0.0]}});
blockColor = vertcat(blockColor, {'Blue',      {[0.0, 0.0, 1.0]}});
blockColor = vertcat(blockColor, {'Orange',    {[1.0, 0.01, 0.0]}});
blockColor = vertcat(blockColor, {'Purple',    {[1.0, 0.0, 0.5]}});
blockColor = vertcat(blockColor, {'GameOver',  {[1.0, 0.0, 0.0]}});
blockColor = vertcat(blockColor, {'None',      {[0.02, 0.02, 0.02]}});

% �Ֆʂ̕`��T�C�Y
boardDisplaySize = struct( ...
    'width',  10, ...
    'height', 20 ...
);

% �ՖʃT�C�Y
boardSize = struct( ...
    'width',  boardDisplaySize.width + 2, ...
    'height', boardDisplaySize.height + 2 ...
);

% �E�B���h�E�̃T�C�Y
windosSize = struct( ...
    'width',  blockSize * boardDisplaySize.width, ...
    'height', blockSize * boardDisplaySize.height ...
);

% �E�B���h�E��
windowTitle = 'Tetris';

% Sleep����
sleepTime = 1/60;

% �T���v�����O�J�E���g
keyinputSampleFrame = 5;
fallSampleFrame = 10;

% �e�g���X�p�����[�^
tetrisParam = struct( ...
    'blockSize',           blockSize, ...
    'boardSize',           boardSize, ...
    'boardDisplaySize',    boardDisplaySize, ...
    'windosSize',          windosSize, ...
    'windowTitle',         windowTitle, ...
    'blockColor',          blockColor, ...
    'blockColorNum',       size(blockColor, 1), ...
    'sleepTime',           sleepTime, ...
    'fallSampleFrame',     fallSampleFrame, ...
    'keyinputSampleFrame', keyinputSampleFrame ...
);

for i = 1:10
    getIndex = 0;
    setIndex = 0;
    name = '';
end
checkVariableName();

end
