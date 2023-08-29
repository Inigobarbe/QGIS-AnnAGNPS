#include "generalcontrol.h"
#include "ui_generalcontrol.h"

GeneralControl::GeneralControl(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::GeneralControl)
{
    ui->setupUi(this);
}

GeneralControl::~GeneralControl()
{
    delete ui;
}
