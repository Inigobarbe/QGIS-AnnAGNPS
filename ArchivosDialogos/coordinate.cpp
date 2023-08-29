#include "coordinate.h"
#include "ui_coordinate.h"

Coordinate::Coordinate(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Coordinate)
{
    ui->setupUi(this);
}

Coordinate::~Coordinate()
{
    delete ui;
}
