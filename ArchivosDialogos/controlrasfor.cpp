#include "controlrasfor.h"
#include "ui_controlrasfor.h"

controlrasfor::controlrasfor(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::controlrasfor)
{
    ui->setupUi(this);
}

controlrasfor::~controlrasfor()
{
    delete ui;
}
