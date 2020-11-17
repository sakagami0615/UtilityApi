%----------------------------------------------------------------------
% Name : checkVariableName
% Desc : mスクリプトに使用している変数名が適切かをチェックする

% How to : チェックしたいスクリプト内の末尾に「checkVariableName();」の分を追加し、
%          スクリプトを実行する
%
% Detail : チェック内容は下記の通り
%          ・インデックス変数名チェック(i,j,kなどの名前が使われていないか)
%          ・短い変数名チェック(a,bなどの短すぎて用途が不明な変数がないか)
%          ・意図が理解できない変数名チェック(Name,ValueなどMATLABのサンプルを流用したような変数がないか)
%----------------------------------------------------------------------

% 変数名を取得
variableStructs = whos;
variableNames = arrayfun(@(idx) variableStructs(idx).name, 1:length(variableStructs), 'UniformOutput',false);

% チェック対象のファイルパスを取得
[ST, I] = dbstack('-completenames', 1);
filePath = ST(1).file;

checkVariableNameCore(filePath, variableNames);

%% 変数名チェック用のコア関数
function checkVariableNameCore(filePath, variableNames)

nglog = {};

% 各種チェックを実施
nglog_tmp = chkeckIndexVariableName(variableNames);
if ~isempty(nglog_tmp)
    nglog = vertcat(nglog, nglog_tmp);
end

nglog_tmp = chkeckShortVariableName(variableNames);
if ~isempty(nglog_tmp)
    nglog = vertcat(nglog, nglog_tmp);
end

nglog_tmp = chkeckUnintentionVariableName(variableNames);
if ~isempty(nglog_tmp)
    nglog = vertcat(nglog, nglog_tmp);
end

if ~isempty(nglog)
    nglog = vertcat('--------------------', nglog);
    nglog = vertcat('result:NG', nglog);
    nglog = vertcat(strcat('file:', filePath), nglog);
else
    nglog = vertcat('result:OK', nglog);
    nglog = vertcat(strcat('file:', filePath), nglog);
end

% 表示
for index = 1:length(nglog)
    disp(nglog{index})
end
end


%% インデックス変数名のチェック関数
function nglog = chkeckIndexVariableName(variableNames)

nglog = {};
for index = 1:length(variableNames)
    switch(variableNames{index})
    case 'i'
        nglog = vertcat(nglog, '・Do not use "i" in index variable names');
    case 'j'
        nglog = vertcat(nglog, '・Do not use "j" in index variable names');
    case 'k'
        nglog = vertcat(nglog, '・Do not use "k" in index variable names');
    case 'l'
        nglog = vertcat(nglog, '・Do not use "l" in index variable names');
    case 'm'
        nglog = vartcat(nglog, '・Do not use "m" in index variable names');
    case 'n'
        nglog = vertcat(nglog, '・Do not use "n" in index variable names');
    end
end

if ~isempty(nglog)
    nglog = vertcat('■chkeckIndexVariableName NG Log', nglog);
end

end


%% 短い変数名のチェック関数
function nglog = chkeckShortVariableName(variableNames)

nglog = {};
for index = 1:length(variableNames)
    variableName = variableNames{index};
    if length(variableName) < 5
        nglog = vertcat(nglog, strcat('Variable name "', variableName, '" is too short (at least 5 characters or more)'));
    end
end

if ~isempty(nglog)
    nglog = vertcat('■chkeckShortVariableName NG Log', nglog);
end

end

%% 意図が理解できない変数名のチェック
function nglog = chkeckUnintentionVariableName(variableNames)

PerfectMmatchString = {'Objects', 'objects', 'Object', 'object', ...
                       'Objs', 'objs', 'Obj', 'obj', ...
                       'Systems', 'systems', 'System', 'system', ...
                       'Names', 'names', 'Name', 'name', ...
                       'Values', 'values', 'Value', 'value', ...
                       'Blocks', 'blocks', 'Block', 'block', ...
                       'Blks', 'blks', 'Blk', 'blk', ...
                       'Rets', 'rets', 'Ret', 'ret'};

PartialMatch = {'Gets', 'gets', 'Get', 'get', ...
                'Sets', 'sets', 'Set', 'set'};

nglog = {};
for index = 1:length(variableNames)
    variableName = variableNames{index};
    for matchIndex = 1:length(PerfectMmatchString)
        if strcmp(variableName, PerfectMmatchString{matchIndex})
            nglog = vertcat(nglog, strcat('Variable name "', variableName, '" is not appropriate (the purpose of use is unknown)'));
        end
    end
end

for index = 1:length(variableNames)
    variableName = variableNames{index};
    for matchIndex = 1:length(PartialMatch)
        if contains(variableName, PartialMatch{matchIndex})
            nglog = vertcat(nglog, strcat('Variable name "', variableName, '" is not a proper name (change "', PartialMatch{matchIndex}, '" to another word)'));
        end
    end
end

if ~isempty(nglog)
    nglog = vertcat('■chkeckUnintentionVariableName NG Log', nglog);
end

end
