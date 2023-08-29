#ifndef CONTROLTOPAGNPS_H
#define CONTROLTOPAGNPS_H

#include <QDialog>

namespace Ui {
class ControlTOPAGNPS;
}

class ControlTOPAGNPS : public QDialog
{
    Q_OBJECT

public:
    explicit ControlTOPAGNPS(QWidget *parent = nullptr);
    ~ControlTOPAGNPS();

private:
    Ui::ControlTOPAGNPS *ui;
};

#endif // CONTROLTOPAGNPS_H
