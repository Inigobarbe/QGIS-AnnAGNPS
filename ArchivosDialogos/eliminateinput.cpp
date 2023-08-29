#include "eliminateinput.h"
#include "ui_eliminateinput.h"

EliminateInput::EliminateInput(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::EliminateInput)
{
    ui->setupUi(this);
}

EliminateInput::~EliminateInput()
{
    delete ui;
}
